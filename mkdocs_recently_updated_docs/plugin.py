from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs_document_dates.utils import load_git_last_updated_date, get_recently_updated_files


class RecentlyUpdatedPlugin(BasePlugin):
    config_scheme = (
        ('limit', config_options.Type(int, default=10)),
        ('exclude', config_options.Type(list, default=[]))
    )

    def __init__(self):
        super().__init__()

        self.recent_docs_html = None

    def on_env(self, env, config, files):
        limit = self.config.get('limit')
        exclude_list = self.config.get('exclude')

        docs_dir = Path(config['docs_dir'])
        git_updated_dates = load_git_last_updated_date(docs_dir)
        recently_updated_data = get_recently_updated_files(git_updated_dates, files, exclude_list, limit, True)

        # 渲染HTML
        self.recent_docs_html = self._render_recently_updated_html(recently_updated_data)

        return env

    def _render_recently_updated_html(self, recently_updated_data):
        default_template_path = Path(__file__).parent / 'templates' / 'recently_updated_group.html'
        template_dir = default_template_path.parent
        template_file = default_template_path.name

        # 加载模板
        env = Environment(
            loader = FileSystemLoader(str(template_dir)),
            autoescape = select_autoescape(["html", "xml"])
        )
        template = env.get_template(template_file)

        # 渲染模板
        return template.render(recent_docs=recently_updated_data)

    def on_post_page(self, output, page, config):
        if '\n<!-- RECENTLY_UPDATED_DOCS -->' in output:
            output = output.replace('\n<!-- RECENTLY_UPDATED_DOCS -->', self.recent_docs_html or '')
        return output

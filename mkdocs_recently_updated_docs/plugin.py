from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs_document_dates.utils import get_recently_updated_files


class RecentlyUpdatedPlugin(BasePlugin):
    config_scheme = (
        ('limit', config_options.Type(int, default=10)),
        ('exclude', config_options.Type(list, default=[])),
        ('template', config_options.Type(str, default=''))
    )

    def __init__(self):
        super().__init__()

        self.recent_docs_html = None

    def on_nav(self, nav, config, files):
        limit = self.config.get('limit')
        exclude_list = self.config.get('exclude')
        template_path = self.config.get('template')

        docs_dir = Path(config['docs_dir'])

        # 获取 docs 目录下最近更新的文档
        _, recently_modified_files = get_recently_updated_files(docs_dir, files, exclude_list, limit, True)

        # 渲染HTML
        self.recent_docs_html = self._render_recently_updated_html(docs_dir, template_path, recently_modified_files)

        return nav

    def _render_recently_updated_html(self, docs_dir, template_path, recently_updated_data):
        # 获取自定义模板路径
        if template_path:
            user_full_path = docs_dir / template_path

        # 选择模板路径
        if template_path and user_full_path.is_file():
            template_dir = user_full_path.parent
            template_file = user_full_path.name
        else:
            # 默认模板路径
            default_template_path = Path(__file__).parent / 'templates' / 'recently_updated_list.html'
            template_dir = default_template_path.parent
            template_file = default_template_path.name

        # 加载模板
        env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(["html", "xml"])
        )
        template = env.get_template(template_file)

        # 渲染模板
        return template.render(recent_docs=recently_updated_data)

    def on_page_markdown(self, markdown, page, config, files):
        if '\n<!-- RECENTLY_UPDATED_DOCS -->' in markdown:
            markdown = markdown.replace('\n<!-- RECENTLY_UPDATED_DOCS -->', self.recent_docs_html or '')
        return markdown

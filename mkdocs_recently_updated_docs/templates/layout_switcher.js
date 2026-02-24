// 最近更新 - 布局切换器 (Layout Switcher)
function initLayoutSwitcher() {
    const grids = document.querySelectorAll('.article-grid');
    if (!grids.length) return;

    const savedLayout = localStorage.getItem('dd_recent_docs_layout') || 'grid';

    grids.forEach(grid => {
        // 应用初始布局
        grid.classList.toggle('is-list', savedLayout === 'list');
        grid.classList.toggle('is-detail', savedLayout === 'detail');


        // 查找或创建切换器容器
        let switcher = grid.previousElementSibling;
        if (!switcher || !switcher.classList.contains('article-layout-switcher')) {
            // 如果模板中没写，可以动态注入，但建议写在模板里以保证 UI 一致性
            return;
        }
        const listBtn = switcher.querySelector('.layout-list-btn');
        const detailBtn = switcher.querySelector('.layout-detail-btn');
        const gridBtn = switcher.querySelector('.layout-grid-btn');

        const updateActiveBtn = (layout) => {
            if (listBtn) listBtn.classList.toggle('is-active', layout === 'list');
            if (detailBtn) detailBtn.classList.toggle('is-active', layout === 'detail');
            if (gridBtn) gridBtn.classList.toggle('is-active', layout === 'grid');
        };
        updateActiveBtn(savedLayout);


        const setLayout = (layout) => {
            grid.classList.remove('is-list', 'is-detail');
            if (layout !== 'grid') {
                grid.classList.add(`is-${layout}`);
            }
            localStorage.setItem('dd_recent_docs_layout', layout);
            updateActiveBtn(layout);
        };
        if (listBtn) {
            listBtn.onclick = () => {
                setLayout('list');
                listBtn.blur();
            };
        }
        if (detailBtn) {
            detailBtn.onclick = () => {
                setLayout('detail');
                detailBtn.blur();
            };
        }
        if (gridBtn) {
            gridBtn.onclick = () => {
                setLayout('grid');
                gridBtn.blur();
            };
        }
    });
}

if (window.document$ && !window.document$.isStopped) {
    window.document$.subscribe(initLayoutSwitcher);
} else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLayoutSwitcher);
} else {
    initLayoutSwitcher();
}

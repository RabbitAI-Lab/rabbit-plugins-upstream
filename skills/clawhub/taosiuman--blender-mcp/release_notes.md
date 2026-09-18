## v2.5.5 - 5.3 Alpha API 增量更新 (09-16)

基于 Blender 官方 API change_log 第四次扫描，新增 3 项 API。

### 新增 API

- ✅ **RenderEngine.bl_write_viewport_depth** - 自定义渲染引擎写入视口深度缓冲
  - 插件开发价值：自定义渲染器插件可以输出深度信息
- ✅ **FileHandler.label_with_extensions** - 文件处理器显示带扩展名的标签
  - 插件开发价值：导入/导出插件可以显示更友好的文件类型标签
- ✅ **UILayout.label_markdown** - UI 布局中渲染 Markdown 格式文本
  - 插件开发价值：UI 插件可以使用 Markdown 格式化文本显示

### 对比

- v2.5.4 → v2.5.5: +3 项 API
- 均为 UI/渲染/文件处理增强，无破坏性变更

### 兼容性

- Blender 5.1+ ✅
- Blender 5.2 LTS ✅
- Blender 5.3 Alpha ✅

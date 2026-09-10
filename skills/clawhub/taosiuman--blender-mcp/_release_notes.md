## Blender MCP Skill v2.3.0

### Blender 5.3 Alpha 支持

新增 20 项 API 文档：
- Python API 6 项：NodeTreeInterface.root_panel, UILabel_multiline(), WindowManager.try_activate_rna_button(), mathutils.KDTree 2D, undo_stack, all_ids 顺序警告
- Geo Nodes 13 项：Combine List, Rasterize Points, Deactivate Voxels, Grid Topology Boolean 等
- GPU 兼容性 1 项：GPUBatch.draw_instanced 行为变更

### 更新
- CHANGELOG 完整记录
- 兼容性警告：bpy.data.all_ids 顺序变更
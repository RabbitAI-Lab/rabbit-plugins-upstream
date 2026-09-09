## v2.5.2 - 版本修复

**发布日期**: 2026-09-09

### 修复内容
- 修复 GitHub 和 ClawHub 版本号不一致问题
- 新增发布前版本校验流程

### 技术细节
- Cron 任务发现 18 个新 API 后尝试发布 v2.5.1
- GitHub 接受（Contents API 覆盖）
- ClawHub 拒绝（版本已存在）
- 根因：Cron prompt 缺少版本校验步骤

### 改进
- 更新 \prompts/blender-mcp-daily-research-and-publish.md\
- 新增"阶段三：发布前版本校验"
- 确保每次发布前检查各平台版本，避免冲突

**注意**: 此为版本修复版本，功能与 v2.5.1 相同。
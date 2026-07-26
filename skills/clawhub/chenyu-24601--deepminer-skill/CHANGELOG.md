# Changelog

## 1.7.2 (2026-06-26)

### 修复
- 明确所有异步任务（含 `media_download_task_register`）注册后均返回 `PENDING`，需立即执行 `task lifecycle --action start` 才会真正执行，不会自动开始
- 记录 `task info` 的已知 CLI bug：`estimate_time` 字段返回数字时 Go 解析报错，任务本身不受影响，可改用 `thread result` 查状态

## 1.2.0 (2026-04-10)

### 改进
- 优化了 async_tag_task 状态处理逻辑
- 改进了 ask_human 状态的判断机制
- 添加了更详细的轮询策略说明
- 完善了错误处理文档

### 文档
- 更新了 SKILL.md 使用说明
- 添加了 response-structure.md 参考文档

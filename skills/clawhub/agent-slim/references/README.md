# 参考文档路由

入口是 `routing-index.md`（按问题选文件）；本文件只说明 references 与 docs 的分工。

- `context-model.md`：Hot/Warm/Cold 与 Token/磁盘账本的详细定义。
- `adapter-contract.md`：宿主适配器的最小接口、能力和错误约定。
- `integration-routing.md`：Ponytail、Skill Architect、Memory Orchestrator 和发布流程的归属、交接数据与降级规则。

`docs/` 保存产品级架构、安全和验收；`references/` 只放需要按需读取的细化说明。不得在这里复制 Memory Orchestrator 的阈值或 Ponytail、Skill Architect 的执行算法。

- `../docs/audit-json-contract.md`：只读审计的稳定 JSON 字段、退出码和读取边界。

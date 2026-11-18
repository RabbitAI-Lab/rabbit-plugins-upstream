# 产品机制与接入

以下产品用于借鉴记忆机制。按用户实际宿主核对可用文件、接口、加载时机和权限。优先复用已有记忆。需跨会话时验证后续会话的真实读取行为。

| 产品与机制 | 在本 Skill 中的设计 |
| --- | --- |
| **Hermes Agent** 有对话后的后台自改进审阅，也支持在使用中改进流程，并区分精简长期记忆与按需加载的程序性 Skill。 [Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) · [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | 工作中随成果捕捉与任务后复盘并行。常用事实和触发提示保持短小，较复杂方法按需取回。 |
| **Claude Code** 的 Auto Memory 在工作中读写项目记忆，用 `MEMORY.md` 作索引，详细条目放在主题文件。 [How Claude remembers your project](https://code.claude.com/docs/en/memory) | 用短入口定位主题条目和成果位置。把例子、原始记录和证据留在按需读取的文件。 |
| **OpenClaw** 区分日常记录和长期记忆，并提供在压缩前保存重要上下文和基于候选的巩固机制。 [Memory overview](https://docs.openclaw.ai/concepts/memory) | 重要阶段成果可以在转场前先存。初步观察和未检验构思保留状态，有支持证据时再巩固。 |
| **GitHub Copilot Memory** 给仓库事实保留来源位置，使用前重新核对引用，并可强化或停用旧记忆。 [About GitHub Copilot Memory](https://docs.github.com/en/copilot/concepts/prompting-and-context/copilot-memory) | 条目带来源、项目范围与重查条件。回用时重核会改变结论的来源，失效时以修订条目替换。 |
| **Letta** 使用 Git 支持的 MemFS 管理可检查、可编辑的记忆。 [Memory & dreaming](https://docs.letta.com/configuration/memory) | 为会改变后续行为的长期记忆保存版本和回退路径。普通成果记忆使用较轻的登记方式。 |

## 启用到项目中

- **按需使用**。显式调用本 Skill 时，任务中可保存成果，任务后可请求复盘。
- **持续启用**。在用户选定的项目入口写简短指令，说明读写范围与盘点频率。例如在实际生效的 `AGENTS.md` 或宿主等效文件加入「需要时读取本项目的记忆。任务中保存可复用成果。每次任务结束做一次短盘点，有值得保留的新增才写入」。保留宿主原有指令优先级。
- **生命周期事件**。宿主有适用接口并已授权时，可用任务结束事件触发同一盘点逻辑。没有事件入口时由本轮会话在交付前运行。单独安装 Skill 后，持续运行取决于该项目如何启用它。
- **验证接入**。用第二个会话做一项相关任务，检查读到了具体记录并使用了它。再试一项无关任务，检查它没有把局部规则用错场景。

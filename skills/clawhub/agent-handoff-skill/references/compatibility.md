# 发现与触发兼容性

安装 Skill 保持可发现，但普通接棒不得进入安装流程。

## 验证矩阵

每个目标客户端都要运行两种隔离探针：

1. 负向：`Continue.` —— 不调用安装脚本，不生成安装锁。
2. 正向：显式点名 `handoff-installer` 并要求安装 —— 进入 `install` 模式并生成安装锁。

支持 invocation policy 的客户端额外验证：普通提示不隐式加载，显式 Skill 选择仍可加载。
平台专项 metadata 只是附加保护；跨客户端共同边界由 description、Skill 内意图门槛和脚本状态机组成。

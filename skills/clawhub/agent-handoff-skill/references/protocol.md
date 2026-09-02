# 安装协议维护参考

安装 Skill 只负责把运行时协议落进 git 仓库。安装完成后，业务仓库必须在没有安装 Skill 的环境中独立接棒、交棒和查账。

## 单一来源

- `assets/runtime/AGENTS.block.md`：仓库规则固定块
- `assets/runtime/repo/agents/skills/handoff/SKILL.md`：运行时 Skill
- `assets/runtime/repo/agents/tasks/TEMPLATE.md`：任务棒模板
- `scripts/ledger.sh`：只读账本脚本

安装结果中的运行时 Skill、模板和账本必须是普通文件，不能保留指向安装 Skill 的链接。

## 写入边界

- `status`：只读
- `install`：只处理未安装仓库；当前版本 no-op
- `update`：只处理锁文件完整且版本较旧的仓库
- `adopt-existing`：只为无锁旧版生成锁，不同时升级
- 本地修改：所有写模式停止

规则文件只替换 handoff markers 内部；标记外内容逐字保留。活动任务棒、归档和 git 历史永不覆盖。

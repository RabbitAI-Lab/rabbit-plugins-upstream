# Agent OS Asset

English is normative; ZH-CN is the faithful companion translation. / 英文是规范文本，简体中文是忠实配套翻译。

Turn forgotten files across your computer into privacy-aware, reviewable assets that AI agents can reliably retrieve and use—helping build a personal second brain and durable digital knowledge twin. / 将电脑中长期吃灰的各类文件转化为经过隐私检查与人工复核、可被 AI Agent 可靠检索和调用的资产，用于构建个人第二大脑与可持续演进的数字知识分身。

`agent-os-asset` supports mixed documents, archives, code repositories, datasets, and media while preserving review, privacy, and execution gates. / `agent-os-asset` 支持混合文档、归档、代码仓库、数据集与媒体文件，同时保留 review、隐私与执行门禁。

This vendor-neutral Agent Skills package works with Codex, Claude Code (CC), OpenClaw, Hermes, WorkBuddy, and other agents that can load `SKILL.md`, preserve bundled child directories, and run local tools. Product-specific metadata under `agents/` is optional and does not define the core workflow. / 这个供应商中立的 Agent Skills package 适用于 Codex、Claude Code（CC）、OpenClaw、Hermes、WorkBuddy，以及其他能够加载 `SKILL.md`、保留随包 child directories 并运行本地工具的 Agent；`agents/` 下的产品专属 metadata 是可选项，不定义核心流程。

The root Skill is the only public entrypoint and bundles three internal child Skills. / 根 Skill 是唯一公开入口，并随包包含三个内部 child Skills。

- `agent-readable-doc`: extraction and semantic materialization / 提取与语义物化。
- `kb-review`: value review and lifecycle decisions / 价值 review 与生命周期决策。
- `second-brain`: final indexing and retrieval / 最终索引与检索。

## Install / 安装

```bash
npx skills add lee-agi/agent-os-asset -g -y
```

The complete suite installs as one package. Invoke `$agent-os-asset`; the root Skill loads child instructions only when their stage is required. Runtimes without the `skills` CLI may clone or copy the repository and load root `SKILL.md` directly. / 完整套件作为一个 package 安装；调用 `$agent-os-asset` 后，根 Skill 只在对应阶段需要时加载 child instructions。没有 `skills` CLI 的运行时可以 clone 或复制仓库，并直接加载根 `SKILL.md`。

## Safety Defaults / 默认安全策略

- Discovery and planning are read-only by default / Discovery 与 planning 默认只读。
- Extraction, archive, review apply, deletion, synchronization, remote model use, and indexing require explicit enablement / Extraction、archive、review apply、deletion、synchronization、remote model use 与 indexing 都需要显式启用。
- PII and secret-like paths are excluded from content extraction / PII 与 secret-like paths 排除在正文提取之外。
- Generated indexes, local logs, review decisions, and personal source material are not distributed / Generated indexes、local logs、review decisions 与 personal source material 不参与发布。
- macOS automation is optional; the core pipeline works without LaunchAgent or AppleScript / macOS automation 是可选项；核心 pipeline 不依赖 LaunchAgent 或 AppleScript。
- The local review server binds only to loopback and starts read-only; file opening, decision saving, and decision application require explicit flags plus an ephemeral session token / 本地 review server 只绑定 loopback 且默认只读；打开文件、保存 decision 与应用 decision 都需要显式 flags 和 ephemeral session token。

## Verification / 验证

```bash
uvx --from pytest pytest -q
python3 scripts/asset_pipeline.py --self-test
```

## License / 许可证

Apache-2.0.

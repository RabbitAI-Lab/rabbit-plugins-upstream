# 贡献指南 / Contributing Guide

<!-- oss-scaffold settings profile 骨架。依据：Tencent org 298 仓中 93 仓（31.2%）根目录存在
     CONTRIBUTING，是覆盖率第二高的社区组件（仅次于 issue 模板与 CI 之间的位置见 PROFILE.md §1）。
     本文件是结构骨架：各仓的具体条款（CLA、评审时限、分支模型）扫描未抓取正文，
     使用时按仓库实际填写 TODO 处。 -->

感谢关注本项目！欢迎通过 issue 与 pull request 参与贡献。本文说明参与方式与流程规范。

## 参与方式 / Ways to contribute

- **报告缺陷**：使用 Bug 反馈模板提交 issue，附上复现步骤与环境信息。
- **功能建议**：使用功能建议模板提交 issue，说明你的使用场景。
- **代码贡献**：认领带 `help wanted` 标签的 issue，提交 PR。
- **文档改进**：README、示例、注释的修正都受欢迎，小改动可直接提 PR。

## 提交前准备 / Before you start

1. Fork 本仓库并克隆到本地。
2. 阅读 README 中的「快速开始」，确保本地构建与测试可以跑通：<!-- TODO: 写入本仓的构建/测试命令 -->
3. `git checkout -b feat/your-feature` 从最新主分支拉出特性分支。

## 提交规范 / Commit convention

<!-- org 实测：Shadow 在 CI 里用 commitlint 强制提交日志格式（「提交日志格式化检查」），
     wepy 提供 CONTRIBUTING_COMMIT.md 单独约束 commit。建议采用 Conventional Commits： -->

提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
<type>(<scope>): <subject>

feat(core): add xxx support
fix(ui): resolve yyy on zzz
docs: update README quick start
```

常用 type：`feat` / `fix` / `docs` / `test` / `refactor` / `perf` / `chore`。

## Pull Request 流程 / PR workflow

1. 确认对应 issue 已存在；没有则先建 issue 说明动机。
2. 一个 PR 只做一件事，改动保持最小。
3. 保证 CI 通过（构建、测试、格式检查）<!-- TODO: 按本仓 ci-*.yml 的检查项列举 -->。
4. PR 描述写清楚改了什么、为什么改、如何验证。
5. 等待维护者评审；如需补充修改，直接向该分支追加 commit 即可。

## 代码风格 / Code style

<!-- org 实测：ncnn 提供 .clang-format + code-format CI 强制格式；
     Tendis 用 cpplint + clang-format 增量检查；teamai-cli 用 lint + tsc。 -->

- 遵循仓库内的格式化配置（如 `.clang-format`、`.editorconfig`、lint 配置）。
- 新代码需要带对应测试；修 bug 请附回归测试。
- 公开 API 变更需同步更新文档与示例。

## 行为准则 / Code of conduct

请保持友善与尊重，对事不对人。技术讨论聚焦事实与数据。

## 许可 / License

<!-- org 实测：76% 的腾讯开源仓使用非标准文本 license（LICENSE.txt / NOASSERTION），
     少数为 MIT / Apache-2.0。提交贡献即表示同意你的贡献按本仓 LICENSE 文件授权。 -->

提交 PR 即表示你同意你的贡献将按照本仓库 [LICENSE](./LICENSE) 授权。<!-- TODO: 如仓库需要 CLA，在此说明 -->

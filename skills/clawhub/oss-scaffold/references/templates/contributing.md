<!-- CONTRIBUTING 模板。骨架+占位符；命令必须真实可跑（Agent-Memory#939 教训：不写不存在的分支名）；回应承诺的语气按 oss-persona §2 直接风格执行。默认英文，中文版 CONTRIBUTING.zh-CN.md 对照（oss-voice §1）。 -->

# Contributing to {{project_name}}

Thanks for your interest in contributing.

## Getting Started

1. Fork the repository and clone your fork:

```bash
git clone https://github.com/{{your_fork_owner}}/{{project_name}}.git
cd {{project_name}}
```

2. Create a feature branch from `main`:

```bash
git checkout -b feat/your-feature main
```

## Making Changes

- Keep PRs focused: one PR addresses one issue or one topic.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): description` — e.g. `docs(install): fix broken download link`, `fix(pull): handle empty entry list`.
- Add or update tests for the code you change.

## Verifying Changes

Run these before opening a PR:

```bash
{{lint_cmd}}
{{test_cmd}}
```

For documentation-only changes, state in the PR: `Documentation-only change; no runtime test suite run.`

## Opening a PR

1. Push your branch and open a PR against `main`.
2. Fill in the PR template (`.github/PULL_REQUEST_TEMPLATE.md`).
3. Make sure CI passes.

## Reporting Issues

Use the issue templates (`.github/ISSUE_TEMPLATE/`). Include version, environment, and steps to reproduce. We respond to issues within {{response_sla}} on business days.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).

<!-- PR 模板。骨架+占位符；验证段写实证（命令+通过数字，oss-voice §3），AI 披露按 oss-contribution R17 政策执行。默认英文。 -->

## Description

{{pr_description}}

## Related Issues

Fixes #{{issue_number}}
<!-- 或 Refs #{{issue_number}}：部分关联用 Refs，只有逐现象核对全部处理才用 Fixes -->

## Type of Change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that changes existing behavior; changelog entry under Breaking Changes)
- [ ] Documentation update

## How Has This Been Tested?

{{test_evidence}}
<!-- 写实证：贴命令 + 通过数字，如 `{{test_cmd}}` → 290 files, 4313 passed, 1 skipped；纯文档改动写 Documentation-only change; no runtime test suite run. -->

## Checklist

- [ ] Code follows the project's style guidelines (`{{lint_cmd}}` passes)
- [ ] Self-review completed
- [ ] Comments added for non-obvious logic
- [ ] Corresponding changes made to documentation (doc drift is a bug)
- [ ] No new warnings introduced

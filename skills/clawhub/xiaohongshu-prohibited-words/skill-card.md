## Description:

小红书违禁词离线检测与词库维护，使用纯本地词库和扫描脚本在发布前检查标题、正文和标签中的高风险用词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketing operators, and agent workflows use this skill to scan Xiaohongshu draft titles, body copy, and tags before publishing. It also guides maintenance of an offline prohibited-word list with P0/P1/P2 severity guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The maintained prohibited-word list may create false positives or reflect account-specific publishing assumptions.

Mitigation: Review and calibrate the word list before relying on it for a publishing workflow, and downgrade or remove terms that are confirmed to be safe.

Risk: Offline pattern matching can miss new or platform-specific review triggers that are not yet in the maintained list.

Mitigation: Add confirmed misses to the reference list with source, severity, replacement guidance, and date, and supplement the offline scan with normal editorial review.

## Reference(s):

- [Prohibited Words Reference](references/prohibited-words.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and plain-text scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline scan results include P0/P1/P2 findings and exit codes: 0 for pass, 1 for P0 findings, and 2 for runtime error.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter and changelog report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

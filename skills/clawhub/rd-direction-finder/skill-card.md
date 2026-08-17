## Description:

Given an engineering or technical problem description, this skill decomposes R&D needs, searches patent, paper, and web sources, and produces structured R&D directions plus Markdown, JSON, and HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and R&D analysts use this skill to turn engineering problem statements into research direction reports backed by patent, paper, and web evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML and Markdown reports are derived from user input and search results.

Mitigation: Review generated report content before sharing or publishing it.

Risk: The skill uses external patent, paper, and web search tools.

Mitigation: Install and run it only where those searches are expected and permitted, and verify cited sources before relying on results.

Risk: The skill creates local Markdown, JSON, and HTML report files.

Mitigation: Review or override the output path before running in shared or sensitive workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/rd-direction-finder)
- [Output path conventions](artifact/assets/paths.md)
- [Payload JSON schema](artifact/assets/payload-schema.md)
- [Report template](artifact/assets/report-template.md)
- [Workflow reference](artifact/assets/workflow.md)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown report, JSON payload, and rendered HTML report with supporting shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires problem_text and optional max_directions; uses external patent, paper, and web search tools.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

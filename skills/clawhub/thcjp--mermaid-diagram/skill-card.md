## Description:

Generates valid Mermaid diagrams such as flowcharts, sequence diagrams, mind maps, and ER diagrams, with Chinese-language interaction and configurable output style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and workflow authors use this skill to turn structured content or prompts into Mermaid diagrams for documentation, reports, data analysis, and planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file read/write and command execution capabilities beyond basic diagram drafting.

Mitigation: Grant only the file and shell permissions needed for the intended diagram workflow, and run rendering commands in a controlled workspace.

Risk: The publisher has not documented exact command, endpoint, credential, or data-handling boundaries.

Mitigation: Review the skill before installation and avoid granting API credentials or broad shell access until those boundaries are documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/mermaid-diagram)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and Mermaid code, with optional JSON-style status output and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagram content, processing status, style metadata, and troubleshooting notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

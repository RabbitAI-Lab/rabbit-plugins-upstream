## Description:

Routing guide -- when to use `nansen agent` (AI research) vs direct CLI data commands. Use when deciding how to answer a user's research question with Nansen tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this guide to choose between Nansen's AI agent for open-ended blockchain research and direct CLI commands for structured data, while following account, credit, and feedback-submission guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nansen research commands use the account and may consume credits.

Mitigation: Choose direct CLI commands for specific structured-data requests, review the stated credit costs, and reserve the higher-cost agent mode for open-ended synthesis.

Risk: A saved feedback preference may permit product reports to be submitted without asking for approval each time.

Mitigation: Check the current preference before reporting; leave it disabled to review each report, and never enable it automatically.

## Reference(s):

- [Nansen CLI browser-login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)
- [Nansen Agent Guide on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-agent-guide)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Nansen CLI command examples and research-routing recommendations]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

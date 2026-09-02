## Description:

ClawVision-zh turns selected OpenClaw session history into local visual summaries and exports HTML, PNG, Markdown, and PowerPoint files without sending data to external APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users use this skill when they explicitly want to convert a selected conversation into a shareable visual one-page summary and companion exports. It is suited for local session summarization workflows where the user wants HTML, PNG, Markdown, or PowerPoint outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the OpenClaw session selected by the user, and that session may contain private, sensitive, or confidential content.

Mitigation: Confirm the intended session and scope before access, and review generated files before sharing.

Risk: The skill writes local export files and runs local Python and Playwright-based rendering steps.

Mitigation: Install and run only when comfortable granting local file read/write and script execution for the selected export workflow.

Risk: Generated summaries can preserve sensitive details from the source conversation.

Mitigation: Do not export secrets, passwords, tokens, or private identifiers; use a generalized summary or stop if the user does not consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision-zh)
- [Project homepage](https://github.com/monaxamo/clawvision-zh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated local HTML, PNG, Markdown, and PowerPoint files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports selectable language, visual preset, accent color, font, layout strategy, and export format.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter describes ClawVision 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

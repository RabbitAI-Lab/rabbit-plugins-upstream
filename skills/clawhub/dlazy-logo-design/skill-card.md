## Description:

Creates, upgrades, and evaluates logos and brand identity assets with brand-gene analysis, refinement, and multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, improve, or evaluate logos and brand identity materials through dLazy's project-scoped logo-design assistant. It supports new logo tasks, follow-up project sessions, and reference-file based refinement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy hosted services for processing.

Mitigation: Confirm that shared prompts and files are appropriate for upload before invoking the dLazy CLI.

Risk: API key and session data can persist in the local dLazy configuration directory.

Mitigation: Use per-run environment variables when persistence is not desired, and clear sessions or log out after use.

Risk: Broad logo and brand trigger words may route a request to the hosted logo-design workflow unexpectedly.

Mitigation: Confirm user intent before sending brand, logo, or reference-file content to the service.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown with shell commands and generated logo asset references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transparent-background logo assets and multi-context previews through dLazy project sessions.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

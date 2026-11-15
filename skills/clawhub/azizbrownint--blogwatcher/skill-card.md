## Description:

Monitor blogs and RSS/Atom feeds for updates using the blogwatcher CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and individual users use this skill to install and run the blogwatcher CLI for tracking RSS/Atom feed updates, listing articles, and marking articles as read.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Go install metadata fetches the upstream blogwatcher module at its latest version, so future upstream changes can alter what gets installed.

Mitigation: Review the upstream module before deployment and pin a known version when reproducibility or stricter supply-chain control is required.

## Reference(s):

- [blogwatcher GitHub repository](https://github.com/Hyaxia/blogwatcher)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/blogwatcher)
- [ClawHub publisher profile](https://clawhub.ai/user/azizbrownint)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and example CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the external blogwatcher CLI binary; install metadata uses the Go module github.com/Hyaxia/blogwatcher/cmd/blogwatcher@latest.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

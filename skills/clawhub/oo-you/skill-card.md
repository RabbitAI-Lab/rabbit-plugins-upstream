## Description:

You.com (you.com). Use this skill for ANY You.com request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate You.com through an OOMOL-connected account for web search, news search, page-content fetching, cited research, finance research, and account-balance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes direct remote script execution for installing the oo CLI.

Mitigation: Review the installer before running it and install only if OOMOL is trusted.

Risk: Research and finance actions may consume account credits or affect provider-side state.

Mitigation: Confirm payloads and expected effects before running actions marked as write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-you)
- [You.com homepage](https://you.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return You.com connector data as JSON, including execution metadata when actions are run.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

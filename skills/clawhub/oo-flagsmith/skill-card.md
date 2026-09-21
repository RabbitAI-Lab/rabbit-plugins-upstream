## Description:

Flagsmith helps agents read and update Flagsmith feature flag data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Flagsmith feature flags through an OOMOL-connected account. It supports listing flags, retrieving a feature flag, evaluating identity flags and traits, and identifying users with optional trait updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include a one-line remote CLI installer that should be reviewed before use.

Mitigation: Review OOMOL's oo CLI installation source and prefer an official verified installer or checksum/signature process when available.

Risk: The identify_identity action can change Flagsmith identity traits and evaluated flag state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Flagsmith skill page](https://clawhub.ai/oomol/skills/oo-flagsmith)
- [Flagsmith homepage](https://www.flagsmith.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads and returns JSON execution output from the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

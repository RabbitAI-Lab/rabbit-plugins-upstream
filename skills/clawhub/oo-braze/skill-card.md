## Description:

Braze helps agents search and read Braze campaign and Canvas data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Braze campaigns and Canvases from an already connected OOMOL account without handling raw Braze API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Do not let an agent run installer commands automatically; use a trusted, version-pinned, integrity-checked oo CLI install path.

Risk: The skill can access Braze data through a connected OOMOL account.

Mitigation: Confirm which Braze account and scopes are connected before use, and keep execution limited to the listed read-focused actions unless future write or destructive actions are explicitly confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-braze)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Braze Homepage](https://www.braze.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON from the oo CLI when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

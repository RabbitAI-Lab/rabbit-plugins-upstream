## Description:

Fathom Analytics helps agents read, create, and update Fathom Analytics data through an OOMOL-connected `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Fathom action schemas and operate account, site, event, milestone, visitor, and aggregation workflows through an OOMOL-connected Fathom Analytics account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can run arbitrary code on the user's machine.

Mitigation: Review the setup path before installing, prefer verified and versioned vendor instructions, and do not allow an agent to run remote installer scripts automatically.

Risk: Fathom write actions can create or update sites, events, and milestones.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [Fathom Analytics homepage](https://usefathom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected OOMOL account and live schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

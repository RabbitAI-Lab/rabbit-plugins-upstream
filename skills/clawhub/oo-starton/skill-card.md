## Description:

Starton enables agents to operate Starton IPFS pin workflows through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, inspect, create, pin, and delete Starton IPFS pins while checking each action's live schema before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote oo CLI installer commands that may execute installation scripts.

Mitigation: Review the oo CLI installation path before installing, and prefer a pinned package or verified release.

Risk: The skill can create or delete Starton IPFS pins.

Mitigation: Confirm exact payloads for write actions and require explicit approval before destructive deletes.

## Reference(s):

- [ClawHub Starton Skill](https://clawhub.ai/oomol/skills/oo-starton)
- [Starton Homepage](https://starton.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

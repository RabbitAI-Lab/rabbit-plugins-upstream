## Description:

This skill operates Figma (figma.com) for reading, creating, updating, and deleting Figma data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design collaborators use this skill to inspect Figma files, projects, components, comments, image renders, and related metadata through an OOMOL-connected Figma account. It can also propose write or destructive Figma actions when the user has confirmed the exact target and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may run a remote oo CLI installer script on the user's machine.

Mitigation: Treat CLI setup as local code execution; prefer a verified official package or inspect and verify the installer before running it.

Risk: Write and destructive actions can alter or delete Figma data.

Mitigation: Only allow those actions after reviewing the exact target, payload, and expected effect with the user.

## Reference(s):

- [Figma homepage](https://www.figma.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-figma)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write and destructive Figma actions require user confirmation of the exact target and payload.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

NeetoCal lets agents search and read bookings, scheduling links, and available slots through an OOMOL-connected NeetoCal account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate NeetoCal through OOMOL, including reading bookings, scheduling links, and available slots without handling raw NeetoCal credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require users to install the oo CLI and connect a NeetoCal API key with OOMOL before use.

Mitigation: Review first-time install commands before running them and connect NeetoCal only through the documented OOMOL connection flow.

Risk: Future write-capable NeetoCal actions could change calendar data if added to the connector.

Mitigation: Require user confirmation of the exact payload and effect before running any action marked write or destructive.

## Reference(s):

- [NeetoCal skill page](https://clawhub.ai/oomol/skills/oo-neetocal)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [NeetoCal homepage](https://www.neeto.com/neetocal)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector results as JSON when actions are run.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

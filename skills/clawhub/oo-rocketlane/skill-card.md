## Description:

Rocketlane helps agents search and read Rocketlane projects, tasks, and users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Rocketlane projects, tasks, and users through an OOMOL-connected Rocketlane account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could install unverified code if run automatically.

Mitigation: Do not let an agent run installer commands automatically; download, inspect, and verify the oo CLI installer or use an official safer install method.

Risk: Rocketlane data is accessed through OOMOL as an intermediary.

Mitigation: Install only if the user accepts OOMOL handling Rocketlane access and has reviewed the connected account permissions.

## Reference(s):

- [ClawHub Rocketlane skill page](https://clawhub.ai/oomol/skills/oo-rocketlane)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Rocketlane homepage](https://www.rocketlane.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Rocketlane icon asset](https://static.oomol.com/logo/third-party/rocketlane.svg)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Rocketlane data from read-only get and list actions after live schema inspection.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

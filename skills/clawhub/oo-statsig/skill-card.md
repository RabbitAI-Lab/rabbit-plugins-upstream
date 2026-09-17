## Description:

Use this skill for Statsig search and read requests through the OOMOL connector rather than calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Statsig projects, feature gates, dynamic configs, and segments from an OOMOL-connected account. It is suited for read-oriented Statsig lookup and reporting workflows that need live action schemas before constructing connector payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that the security evidence flags as unverified.

Mitigation: Install the oo CLI manually from independently verified OOMOL documentation and do not let an agent run curl-to-bash or PowerShell iex installers automatically.

Risk: The trigger description is broad while the documented connector actions are read-oriented.

Mitigation: Use the skill for Statsig read and list workflows, inspect the live schema before execution, and require user confirmation before any action that is tagged write or destructive.

## Reference(s):

- [Statsig homepage](https://www.statsig.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Statsig skill](https://clawhub.ai/oomol/skills/oo-statsig)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Statsig connector operations should inspect the live action schema before sending JSON payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

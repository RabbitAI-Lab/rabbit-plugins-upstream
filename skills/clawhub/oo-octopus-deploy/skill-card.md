## Description:

Octopus Deploy connector skill for searching and reading Octopus Deploy data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Octopus Deploy users, spaces, projects, environments, releases, deployments, and server tasks through the OOMOL Octopus Deploy connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet installer commands that could execute unverified remote scripts on the user's machine.

Mitigation: Do not let an agent run curl|bash or irm|iex automatically; prefer the official install guide and verify the installer or package before use.

Risk: The connected Octopus Deploy account and scopes may expose deployment data beyond what the user intends an agent to read.

Mitigation: Confirm the connected account, spaces, and API scopes before use, and limit access to data the agent is allowed to inspect.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-octopus-deploy)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Octopus Deploy Homepage](https://octopus.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Skill Icon](https://static.oomol.com/logo/third-party/octopus_deploy.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill routes Octopus Deploy actions through the oo CLI and returns connector data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Use this skill for Octopus Deploy requests through an OOMOL-connected account, including searching and reading deployment data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, release engineers, and operations teams use this skill to inspect Octopus Deploy users, spaces, projects, environments, releases, deployments, and server tasks through an OOMOL-connected Octopus Deploy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented setup path can execute mutable remote installer scripts on the user's machine.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI through a verified, pinned, or separately reviewed method.

Risk: A connected Octopus Deploy API key may expose more deployment data than the task requires.

Mitigation: Connect only an Octopus Deploy API key with the minimum read permissions needed for the intended workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-octopus-deploy)
- [Octopus Deploy homepage](https://octopus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; read actions can return Octopus Deploy data as JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

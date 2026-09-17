## Description:

Operate Workiz through an OOMOL-connected account to search and read jobs, leads, and active team members without calling the Workiz API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected Workiz account use this skill to inspect connector schemas and retrieve Workiz jobs, leads, and team member data through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI through a verified, trusted method and confirm authentication or connection steps manually.

## Reference(s):

- [Workiz homepage](https://www.workiz.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, text, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live action schemas before submitting JSON payloads and to return connector responses from read actions.]

## Skill Version(s):

1.0.2 (source: evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

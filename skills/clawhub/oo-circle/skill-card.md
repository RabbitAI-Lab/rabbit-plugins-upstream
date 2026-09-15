## Description:

Circle (circle.so). Use this skill for Circle requests that read, create, or update data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Circle communities through an OOMOL-connected account, including retrieving community details, members, space groups, spaces, and posts. The skill also guides agents to inspect live action schemas before constructing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote shell install commands for the oo CLI.

Mitigation: Install the CLI through a verified method and review installer contents before execution.

Risk: The allowed command permission grants broad access to oo CLI commands.

Mitigation: Prefer a narrower permission profile that only allows Circle connector schema inspection and connector run commands.

Risk: Circle write actions can change community data.

Mitigation: Confirm the exact action payload and expected effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-circle)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Circle Homepage](https://circle.so)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata when actions run.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

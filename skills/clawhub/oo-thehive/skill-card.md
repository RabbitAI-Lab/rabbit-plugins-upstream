## Description:

TheHive lets an agent operate an OOMOL-connected TheHive 4 instance by reading alerts and cases and creating alerts and cases through the `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, and incident response teams use this skill to let an agent retrieve TheHive alerts and cases, create new alerts or cases, and inspect live connector schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create TheHive cases and alerts.

Mitigation: Confirm the exact payload and expected effect with the user before approving any case or alert creation.

Risk: The connected TheHive account determines what data and actions the agent can access.

Mitigation: Connect only OOMOL/TheHive accounts with appropriate permissions for the intended workflow.

## Reference(s):

- [ClawHub TheHive skill page](https://clawhub.ai/oomol/skills/oo-thehive)
- [TheHive homepage](https://thehive-project.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector executions return JSON when run with `--json`.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

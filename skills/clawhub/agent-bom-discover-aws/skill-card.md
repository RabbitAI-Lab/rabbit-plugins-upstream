## Description:

Discovers AWS-hosted AI agents and related workloads using operator-controlled credentials and writes canonical agent-bom inventory JSON for optional local scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud operators use this skill to inventory AWS AI agents and workloads in approved accounts and regions, then optionally scan or export findings from the local inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to an AWS profile or role can reveal cloud resource inventory.

Mitigation: Use an operator-approved, short-lived read-only role limited to the intended accounts, regions, and services.

Risk: Generated inventory files may expose details of cloud infrastructure if shared.

Mitigation: Write only to an operator-selected path and review inventory before sharing or exporting it.

## Reference(s):

- [agent-bom project (listed in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)

## Skill Output:

**Output Type(s):** [JSON inventory, Shell commands, Guidance]

**Output Format:** [JSON inventory file and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local scan findings and JSON/SARIF exports when requested by the operator.]

## Skill Version(s):

0.106.1 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

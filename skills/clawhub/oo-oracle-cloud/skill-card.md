## Description:

Oracle Cloud Infrastructure (oracle.com). Use this skill for Oracle Cloud Infrastructure requests that read, create, update, or delete cloud resources through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect and manage Oracle Cloud Infrastructure resources, including tenancy, compartments, networking, compute instances, monitoring, and Oracle Cloud Agent commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can change or permanently remove Oracle Cloud Infrastructure resources.

Mitigation: Confirm the exact payload, target resource, and expected effect with the user before running write or destructive actions.

Risk: Oracle Cloud Agent command execution can run shell or batch scripts on compute instances with the agent service account's privileges.

Mitigation: Review scripts before approval, constrain commands to the requested task, and treat instance-agent execution as a high-impact operation.

Risk: Installing the oo CLI via remote shell commands can expose the environment to unreviewed installer behavior.

Mitigation: Use verified oo CLI installation guidance and avoid blindly piping remote install scripts into a shell.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-oracle-cloud)
- [Oracle Cloud Infrastructure homepage](https://www.oracle.com/cloud/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger read, write, or destructive Oracle Cloud Infrastructure operations through the oo CLI after appropriate user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Seqera (seqera.io). Use this skill for ANY Seqera request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Seqera schemas, read user, workspace, pipeline, and workflow-run information, and launch Seqera workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance can install the oo CLI through a remote shell command.

Mitigation: Review installer provenance manually and install the CLI only through a trusted OOMOL path before allowing the skill to run connector actions.

Risk: The skill can launch Seqera workflows, which may change state or have cost impact.

Mitigation: Require explicit user confirmation of the workflow, workspace, parameters, and expected cost impact before running launch_workflow.

Risk: Connected account permissions determine what Seqera data and actions the agent can access.

Mitigation: Use the least-privileged Seqera account or workspace access appropriate for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-seqera)
- [Seqera homepage](https://seqera.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Seqera icon](https://static.oomol.com/logo/third-party/Seqera.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from Seqera connector actions when commands are executed.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

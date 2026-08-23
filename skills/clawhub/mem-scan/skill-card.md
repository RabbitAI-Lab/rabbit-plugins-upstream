## Description:

Global Memory Bank Deep Scan and Task Analysis Workflow - Multi-repo aware.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scan OpenClaw memory-bank task documentation across workspace and project repositories, identify related tasks or gaps, and recommend documentation updates before changes are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads scoped OpenClaw memory-bank directories that may contain project planning history.

Mitigation: Review the approval request and only run the skill in workspaces where the agent is permitted to inspect memory-bank task documentation.

Risk: Recommended task or implementation-document updates could persist incorrect, duplicate, or misleading planning records.

Mitigation: Approve only the specific recommended actions that match the project context, then verify cross-references, registries, and generated summaries after execution.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown analysis and recommendation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend persistent memory-bank documentation updates, but the workflow requires user approval before changes are applied.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

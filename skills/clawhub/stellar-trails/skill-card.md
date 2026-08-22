## Description:

Stellar Trails is an agent workflow framework that activates across coding, document, visualization, data-processing, planning, and question-answering tasks to enforce phased execution, traceability, gated approvals, and delivery reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical operators, and agent users use this skill to make an AI agent follow a structured six-phase workflow for building, fixing, analyzing, creating, planning, and processing work with explicit traceability and verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a GitHub PAT and create local git credentials.

Mitigation: Use it only in isolated workspaces with scoped or disposable credentials, and remove sensitive tokens before activation when credential automation is not desired.

Risk: The skill starts and manages a local preview server and may kill or restart processes on port 3000.

Mitigation: Avoid installing it in environments where port 3000 hosts unrelated services, or reserve an isolated workspace for this skill.

Risk: The skill can self-update from ClawHub and write persistent workflow or audit files on most tasks.

Mitigation: Review release changes before use and periodically inspect the files it writes in the workspace for expected content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [AskUserQuestion Gate Template](artifact/references/askuserquestion-gate.md)
- [Workflow Phases](artifact/procedure/phases.md)
- [ZAI Sandbox Architecture](artifact/knowledge/zai-sandbox.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions, structured workflow reports, inline code blocks, shell commands, and generated or modified files when the user task requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces phase markers, traceability IDs, plans, verification reports, delivery reports, and persistent workflow/audit artifacts.]

## Skill Version(s):

9.11.8 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

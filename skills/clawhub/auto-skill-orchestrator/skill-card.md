## Description:

Helps an agent plan, select, sequence, verify, and recover workflows across multiple OpenClaw skills when the user explicitly asks for skill orchestration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to coordinate multiple OpenClaw skills for a task, including selecting relevant capabilities, ordering dependencies, verifying results, and recovering when a selected skill fails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route and chain other skills, which may expand the scope of an agent session beyond the user's immediate request.

Mitigation: Use it only when orchestration is explicitly requested, keep the selected skill set minimal, and ask for confirmation before impactful actions.

Risk: Security evidence says the trigger and execution guidance are broad and partly inconsistent about when action may begin.

Mitigation: Require a clear user intent, verify each critical step before continuing, and stop or ask for clarification when the requested workflow is ambiguous.

Risk: Follow-up routing and memory updates could preserve or act on more context than needed.

Mitigation: Limit follow-up routing and memory updates to task-relevant, non-sensitive information and avoid storing credentials or private data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/auto-skill-orchestrator)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text workflow plans with optional command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes and sequences skills; impactful actions should remain subject to user confirmation.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

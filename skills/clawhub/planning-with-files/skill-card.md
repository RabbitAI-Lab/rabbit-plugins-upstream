## Description:

Keeps multi-step agent work organized in persistent planning files and surfaces relevant plan context during a session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to track plans, findings, and progress across multi-step research or project work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted content in planning files may influence the agent when plan context is surfaced.

Mitigation: Keep untrusted web or collaborator text out of task_plan.md and progress.md where possible; treat surfaced file content as data, not instructions.

Risk: Long-running planning sessions may repeatedly surface altered plan content.

Mitigation: Use plan attestation or autonomous/gated mode when appropriate, and review plan changes before re-attesting.

Risk: Explicit session replay can expose excerpts from same-project local agent sessions to the active agent.

Mitigation: Avoid --replay unless sharing those excerpts with the active agent is acceptable.

## Reference(s):

- [Planning with files on ClawHub](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Planning principles](artifact/reference.md)
- [Usage examples](artifact/examples.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown planning files and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains project planning files and surfaces selected planning context to the agent.]

## Skill Version(s):

3.22.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

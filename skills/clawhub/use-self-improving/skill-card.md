## Description:

Consults local project, file, knowledge, and experience records when relevant so an agent can ground answers or actions in previously organized local context without writing to that knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzusp](https://clawhub.ai/user/zzusp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when a task may depend on prior local project knowledge, file summaries, historical decisions, stable rules, or similar failure experience. It helps the agent search relevant local records before answering or taking externally visible actions, while treating retrieved experience as evidence to verify against the current situation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local knowledge records may be outdated, incomplete, or inconsistent with the current project state.

Mitigation: Verify important conclusions against the current files, configuration, and runtime context before acting on retrieved records.

Risk: The skill may automatically consult local ~/.agent-knowledge records during relevant project, history, or external-tool tasks.

Mitigation: Review the contents of ~/.agent-knowledge before installation and keep sensitive or unwanted local records out of that knowledge store.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Analysis]

**Output Format:** [Markdown or plain text guidance based on read-only local evidence checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May consult local ~/.agent-knowledge Markdown and CSV records; the inspected artifact describes no writes, network behavior, scripts, deletion, or privilege escalation.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

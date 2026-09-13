## Description:

A multi-agent deep research workflow that plans, gathers evidence, reviews findings, and writes research outputs for systematic research, competitor analysis, trend analysis, and fact checking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run structured deep-research workflows that decompose broad questions, gather and validate evidence across sources, and assemble reports or other requested formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because the research workflow starts a broad local workbench server with file access, mutation, export, and agent-bridge behavior that is not clearly scoped for a research skill.

Mitigation: Install only when a local research workbench is needed, run it on a trusted machine or network, avoid binding it to 0.0.0.0, and do not attach sensitive directories.

Risk: Remote agent bridges or shared prior session context can expose more workspace or conversation state than intended.

Mitigation: Review bridge settings before enabling them and avoid sharing prior session context unless it is required for the task.

Risk: Configured export commands can mutate files or produce artifacts from attached directories.

Mitigation: Review configured export commands before use and keep sensitive directories outside the workbench scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-deep-research)
- [Deep research workflow definition](artifact/SKILL.md)
- [Evidence schema](artifact/schemas/evidence.schema.md)
- [Plan schema](artifact/schemas/plan.schema.md)
- [Outline schema](artifact/schemas/outline.schema.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Research reports and workflow artifacts, primarily Markdown and JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports quick, normal, and heavy research modes; may start a local research workbench when configured.]

## Skill Version(s):

2026.9.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

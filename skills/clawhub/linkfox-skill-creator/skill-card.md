## Description:

A cross-border e-commerce skill-creation guide that uses a 30-45 minute structured interview to turn operating, product, advertising, logistics, or compliance expertise into agent-executable skill files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lienong1122334](https://clawhub.ai/user/lienong1122334)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border e-commerce experts and skill maintainers use this skill to create, review, or iterate Linkfox-style agent skills from expert SOPs and business know-how without requiring technical authoring knowledge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can generate local skill directories, Python scripts, and helper command instructions that affect the local workspace.

Mitigation: Review generated files and workflows before running any generated scripts or shell commands.

Risk: Delegated Linkfox tool calls can run local helper scripts and persist response data to disk.

Mitigation: Inspect delegated tool paths, parameters, and output locations before using api_call.py, and delete stored outputs that are no longer needed.

Risk: Remote onboarding guidance may direct users to download additional skill packages.

Mitigation: Verify download sources and package contents before installation.

Risk: Interview records and evaluation traces may contain business details, secrets, or sensitive operating knowledge.

Mitigation: Avoid entering secrets or sensitive business information unless local storage of those details is acceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lienong1122334/skills/linkfox-skill-creator)
- [Workflow overview](references/00-workflow-overview.md)
- [Interview process](references/02-stage-1-interview.md)
- [Skill generation rules](references/04-stage-3-generate.md)
- [Delegate discovery](references/06-delegate-discovery.md)
- [Evaluator workflow](references/evaluator/00-workflow-overview.md)
- [Evaluator sub-agent protocol](references/evaluator/08-sub-agent-protocol.md)
- [Interview record schema](references/interview-record-schema.md)
- [Writing style](references/writing-style.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown skill files, reference documents, Python script templates, shell command examples, and structured review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local skill directories, generated scripts, workflow files, interview records, evaluation reports, and delegated tool output files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

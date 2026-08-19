## Description:

meta-openai-whisper is a public meta-skill distilled from openai-whisper that claims to add self-verification, reflection, orchestration, and ongoing learning loops around Whisper-related tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill for openai-whisper-related agent tasks where they want the skill to add reflection and verification prompts around the base workflow. Review the workflow before relying on the claimed self-improvement behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes broad claims about Whisper, self-verification, orchestration, and cross-session learning without an auditable workflow matching those claims.

Mitigation: Review the skill before installing and require concrete, bounded instructions and user controls before relying on these claims.

Risk: The bundled learner script can record operation notes in a local learned_patterns.json file.

Mitigation: Avoid recording sensitive information in learner notes and review stored patterns before sharing or publishing the skill artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-openai-whisper)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

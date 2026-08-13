## Description:

Backfill project timelines, capture key decisions and fixes, and extract reusable process notes from development work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

Developers and repo-aware agent users use this skill to backfill project history, record key decisions and fixes, and turn development work into compact process notes or reusable narrative material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated process notes may include private project names, paths, or internal-only details if the source repository context contains them.

Mitigation: Review generated docs/process content before publishing or sharing the repository, and keep public output free of private names, private paths, and internal-only notes.

Risk: Implicit invocation could create process notes when a user expected the skill to run only on explicit request.

Mitigation: Disable implicit invocation in the agent setup when process notes should be created only after a direct user request.

## Reference(s):

- [Process Guide](PROCESS_GUIDE.md)
- [Example Prompts](references/examples.md)
- [Process Entry Template](references/process-template.md)
- [Process Keeper on ClawHub](https://clawhub.ai/shiyan521/skills/process-keeper)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown process entries, timeline summaries, narrative outlines, and compact recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or append process notes under docs/process when the agent has repository write access.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

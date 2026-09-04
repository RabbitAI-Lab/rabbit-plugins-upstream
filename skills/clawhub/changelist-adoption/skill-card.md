## Description:

Set up and run a per-task changelist practice in any repository with one document per task, a two-level module index, and commit-coupled agent rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[falllee](https://clawhub.ai/user/falllee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to adopt and maintain searchable per-task engineering change records in repositories. It supports first-time setup, per-change entry and index updates, adapted agent rules, and optional index verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adapted agent rules may alter repository workflow, including optional auto-commit behavior.

Mitigation: Review the adapted rule block before adoption and preserve the target repository's commit policy unless an override is deliberate.

Risk: Changelist entries can become misleading if written without real verification evidence.

Mitigation: Require the actual verification command and result before creating an entry or updating the index.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/falllee/skills/changelist-adoption)
- [README](README.md)
- [Agent-instruction rule template](references/agents-rules-template.md)
- [Changelist entry template](assets/entry-template.md)
- [Changelist index template](assets/index-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown documentation, adapted agent-rule text, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent changelist files and index updates in the target repository; includes a local verifier script for index integrity.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

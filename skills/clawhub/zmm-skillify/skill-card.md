## Description:

Creates a reusable local skill from a workflow that has already produced a verified result in the current session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and power users use this skill after completing and validating a workflow to turn the proven process into a reusable local skill with gates, completion criteria, and self-checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skill files could preserve incorrect or misleading guidance if the completed workflow was not reviewed.

Mitigation: Review generated skill files before relying on them.

Risk: The skill may read local skill configuration or memory and persist a short memory record.

Mitigation: Install it only when local workflow-to-skill generation is intended, and use explicit trigger phrases to avoid accidental activation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-skillify)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown skill files and concise guidance, sometimes with shell commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local skill directories and a short memory record when configured.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

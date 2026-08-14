## Description:

Injects a self-improving learning module into WorkBuddy skills so they can record usage outcomes, preferences, and error patterns and suggest future improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to add a reusable learning and reflection loop to WorkBuddy skills, either across a configured set of installed skills or for a single target skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The injector can bulk-modify existing skills under the local WorkBuddy skills directory.

Mitigation: Review the configured target list, back up affected skill directories, and prefer applying the learner to one explicit target at a time.

Risk: The learner can persist user-derived preferences, notes, and troubleshooting details in learned_patterns.json.

Mitigation: Avoid storing secrets, personal data, customer data, filenames, or sensitive notes, and maintain a deletion or redaction process for stored learning data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/skill-self-improve)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with Python scripts, shell commands, and JSON memory-file schema]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates target skill files and can persist learned usage patterns in learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

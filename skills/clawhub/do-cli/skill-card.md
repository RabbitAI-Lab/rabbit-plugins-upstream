## Description:

Guides agents in using the do CLI to capture and review personal tasks, habits, notes, and contacts, and to make related changes through an authorized account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their authorized agents use the CLI to manage personal tasks and habits by capturing tasks, reviewing what is actionable, logging check-ins, and reading related records. Use a scoped API key and confirm before storing sensitive personal details or making broad changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store sensitive personal disclosures about people and change records, including habits.

Mitigation: Get explicit approval before saving personal disclosures or making broad changes; use only the API permissions needed, and check the service destination and retention behavior.

## Reference(s):

- [do source and documentation](https://github.com/robbeverhelst/do)
- [do releases](https://github.com/robbeverhelst/do/releases)
- [Hosted do API](https://do.robbe.work/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Text]

**Output Format:** [Markdown instructions and shell command examples; CLI responses may be JSON or readable text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change personal task, habit, and contact records through the configured account.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

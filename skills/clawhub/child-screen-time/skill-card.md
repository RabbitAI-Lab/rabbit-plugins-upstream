## Description:

Negotiate and enforce screen time contracts with children using a fair AI-mediated system, including per-child daily limits, educational and entertainment budgets, usage tracking, report cards, and earned time for chores, homework, and good behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Parents, guardians, and family-support agents use this skill to operate a local screen-time tracking workflow that separates educational and entertainment use, records earned or deducted minutes, and produces child-specific status summaries, contracts, histories, and report cards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores children's names, ages, screen-time logs, and behavior-related notes in a local file without its own encryption, retention controls, or stricter file permissions.

Mitigation: Use it only on trusted devices, protect the user's home directory and backups, and delete ~/.screen_time.json when the saved family data is no longer needed.

## Reference(s):

- [AAP Screen Time Guidelines](references/aap-guidelines.md)
- [Earned-Time Economy](references/earned-time-economy.md)
- [Source repository](https://github.com/voronindenis5/child-screen-time)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/child-screen-time)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Terminal text output with local JSON state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores child profiles, ages, screen-time logs, and behavior-related notes in ~/.screen_time.json.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

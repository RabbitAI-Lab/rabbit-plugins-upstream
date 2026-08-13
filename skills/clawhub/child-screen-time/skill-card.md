## Description:

Negotiate and enforce screen time contracts with children using a fair AI-mediated system that sets per-child limits, tracks educational and entertainment usage, generates report cards, and grants or extends time for chores, homework, and good behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and family-focused agents use this skill to manage child screen-time budgets, log educational and entertainment usage, negotiate requests for additional time, and summarize compliance trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive child and behavior records in a predictable local file under the user's home directory.

Mitigation: Use pseudonyms where practical, restrict access to the home directory, and delete ~/.screen_time.json when the records are no longer needed.

Risk: The local data file may be exposed through shared, backed-up, or synced home directories.

Mitigation: Avoid running the skill from shared or cloud-synced profiles unless that exposure is acceptable for the family data being recorded.

Risk: Privacy controls and disclosure are limited for data about children and behavior history.

Mitigation: Review the stored data before adoption and establish a retention practice before using the tool with real child profiles.

## Reference(s):

- [AAP Screen Time Guidelines](references/aap-guidelines.md)
- [Earned-Time Economy](references/earned-time-economy.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [CLI text output with Markdown-style command examples and report summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can update local JSON state in ~/.screen_time.json.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

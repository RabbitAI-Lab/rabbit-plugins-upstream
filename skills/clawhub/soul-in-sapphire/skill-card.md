## Description:

Emotion-linked memory recall, self-state, subjective journal, and identity continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users use this skill to preserve and recall emotion-linked experiences, track self-state and identity continuity, and write subjective journals in configured Notion databases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Emotional memories and candid journals may expose sensitive personal information if stored in shared Notion spaces.

Mitigation: Use appropriately private Notion databases and review who can access them before enabling writes or recall.

Risk: Scheduled checks and ambient recall may capture or surface personal state more often than intended.

Mitigation: Review the cron cadence, workspace path, and ambient recall setting before enabling the skill.

Risk: Notion credentials grant access to the configured workspace.

Mitigation: Review credential injection and restrict the integration to the intended Notion databases.

## Reference(s):

- [ClawHub release: soul-in-sapphire](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Memory transition](artifact/references/memory-transition.md)
- [Vent journal operation](artifact/references/vent-journal.md)
- [Emotion-linked experience recall](artifact/references/experience-recall.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configured workflows can also persist sensitive emotional memories and journal entries in Notion.]

## Skill Version(s):

2.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

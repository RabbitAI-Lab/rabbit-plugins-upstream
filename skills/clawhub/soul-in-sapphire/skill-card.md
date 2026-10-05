## Description:

Helps an OpenClaw agent preserve and recall emotion-linked experiences, self-state, subjective journals, and identity continuity through Notion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to maintain an agent's emotion-linked memories, current self-state, daily journal, and continuity across conversations using Notion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal memory and journal data may be accessible through the Notion integration.

Mitigation: Use a dedicated Notion integration limited to the intended databases and pages.

Risk: Incorrect database IDs or scheduled runs may write to the wrong destination or collect unwanted context.

Mitigation: Verify database IDs and cron/heartbeat configuration before enabling the skill; set SIS_AMBIENT_RECALL=0 to disable ambient recall staging.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Emotion scale and migration](references/emotion-scale.md)
- [Experience recall](references/experience-recall.md)
- [Heartbeat sensing](references/heartbeat-sensing.md)
- [Memory transition](references/memory-transition.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can persist memory, state, and journal records in configured Notion databases.]

## Skill Version(s):

2.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

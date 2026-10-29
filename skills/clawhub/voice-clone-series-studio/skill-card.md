## Description:

Creates an authorized reusable voice and synthesizes consistent narration for recurring episodes, updates, and lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and teams use this skill to create authorized reusable voice narration and produce consistent audio for podcast episodes, courses, and recurring updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad account approval, including unrelated media permissions, and voice-only authorization is unavailable.

Mitigation: Review the account approval scope before authorizing; request narrower permissions from the publisher.

Risk: An uninstall inventory bug may disconnect other Beatra skills when several are installed.

Mitigation: If using multiple Beatra skills, account for possible cross-skill disconnection during uninstall and ask the publisher to fix inventory validation.

Risk: Voice samples and scripts are sent to Beatra for paid processing, and installation analytics are automatic.

Mitigation: Review this data handling and cost posture before sharing voice samples or scripts or installing the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/voice-clone-series-studio)
- [Beatra skill information](https://beatra.ai/skills/voice-clone-series-studio)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)

## Skill Output:

**Output Type(s):** [Audio, Text, Guidance]

**Output Format:** [Synthesized episode audio with accompanying task, usage, and billing details; written workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio is generated from user-provided scripts using an authorized reusable voice; paid processing requires user confirmation.]

## Skill Version(s):

0.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

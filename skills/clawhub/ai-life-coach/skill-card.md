## Description:

AI人生教练 is a Socratic life-coaching skill for self-awareness, goal clarity, and action planning, with crisis-first routing, minor-protection boundaries, anti-sycophancy guidance, and local memory for continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for structured life-coaching conversations about uncertainty, emotional blocks, motivation, life direction, parenting, and relationships. It helps users reflect on patterns, clarify goals, and identify next actions without replacing therapy, medical, legal, financial, or emergency support.

### Deployment Geography for Use:

Global; crisis and referral resources are China-specific.

## Known Risks and Mitigations:

Risk: The skill handles sensitive coaching conversations and can store durable local memory notes on the user's device.

Mitigation: Install only on trusted devices, use memory only with consent, avoid shared-device use unless local notes can be inspected and deleted, and use the no-memory option for sensitive sessions.

Risk: Broad emotional triggers may activate coaching behavior during ordinary work or troubleshooting frustration.

Mitigation: Prefer explicit invocation when coaching is intended, and clarify whether the user wants task help or personal coaching when intent is ambiguous.

Risk: The skill promotes a web version whose memory storage is separate from the local-only skill behavior.

Mitigation: Use the promoted website only after separately trusting its server-side storage claims; prefer the local skill when local-only memory is required.

Risk: Built-in crisis and referral resources are China-specific.

Mitigation: International users should rely on local emergency numbers, local mental-health crisis lines, and qualified local professionals.

Risk: The skill is a non-clinical coaching aid and is not a substitute for professional care or emergency response.

Mitigation: For self-harm risk, ongoing severe distress, abuse, medical concerns, legal issues, or major financial decisions, route users to qualified professionals or emergency services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [Promoted web version](https://coach.gzccadinspect.top)
- [FAQ](FAQ.md)
- [Coaching ethics](references/ethics.md)
- [Memory and privacy](references/memory.md)
- [Question methods and signal routing](references/tools.md)
- [Conversation workflow and output format](references/workflow.md)
- [Parent-child relationship module](references/parent_child.md)
- [Intimate relationship module](references/relationship.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational text and optional markdown action blueprints; local markdown memory notes when enabled.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create concise local memory notes with user consent; blueprints are generated only after sufficient conversation material and explicit user agreement.]

## Skill Version(s):

2.3.2 (source: server release evidence; artifact frontmatter and manifest report 2.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

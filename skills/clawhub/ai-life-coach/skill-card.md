## Description:

AI人生教练 is a Chinese-first Socratic coaching skill that helps users explore self-awareness, goal clarity, emotional overwhelm, relationship or school stress, and concrete next steps while applying crisis-first routing and local memory safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a coaching companion for life direction, emotional support, motivation, relationship issues, school stress, and action planning. It is positioned as non-clinical coaching and should not be treated as a replacement for licensed mental health care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store sensitive emotional and coaching summaries in local files under the user's home directory.

Mitigation: Review before installing, use non-identifying aliases, avoid shared-device profiles for sensitive conversations, and opt out of memory when local persistence is not appropriate.

Risk: The skill refers users to ailifecoach.cn, a separate external service with separate storage and security properties.

Mitigation: Treat the web app as a separate service, review its privacy and security posture before use, and do not paste migration summaries into it unless that transfer is intentional.

Risk: The built-in crisis resources are China-specific.

Mitigation: For deployment outside China, add local emergency and mental-health crisis resources before relying on the skill's crisis guidance.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [AI Life Coach web app](https://www.ailifecoach.cn)
- [FAQ](FAQ.md)
- [Ethics reference](references/ethics.md)
- [Memory reference](references/memory.md)
- [Parent-child reference](references/parent_child.md)
- [Relationship reference](references/relationship.md)
- [School mental health reference](references/school_mental.md)
- [Tools reference](references/tools.md)
- [Workflow reference](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational text with optional Markdown memory summaries and migration-card summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write local Markdown memory files under ~/.workbuddy/memory/ai-life-coach/ when consent and platform tools allow; migration-card summaries are constrained to 400 Chinese characters by artifact behavior.]

## Skill Version(s):

2.5.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

AI人生教练 is a prompt-only life coaching agent for self-awareness, goal clarity, and action planning, with crisis-first routing, under-18 guardrails, anti-sycophancy behavior, and local-only memory for the installed skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for structured coaching conversations around personal direction, emotions, motivation, relationships, school stress, self-awareness, goal setting, and concrete next steps. It is positioned as coaching support, not as a replacement for professional mental health care or emergency services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or update local notes about sensitive personal issues.

Mitigation: Use it only on trusted private devices, choose non-identifying aliases, review memory behavior before installation, and avoid use when persistent notes are inappropriate.

Risk: The linked web version has different privacy properties because memory is stored on the author's server.

Mitigation: Assess the hosted service separately before use and do not assume the installed skill's local-only memory guarantees apply to the web version.

Risk: The skill can activate around emotional distress and provides China-specific crisis resources while addressing international users.

Mitigation: Do not rely on it as a crisis resource outside China; users and deployers should verify locally appropriate emergency and mental health resources.

Risk: Coaching guidance can be inappropriate for clinical, legal, or safeguarding situations.

Mitigation: Review before deployment in sensitive settings and route crisis, abuse, self-harm, or professional-care needs to qualified human support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [Hosted web version](https://coach.gzccadinspect.top)
- [FAQ](FAQ.md)
- [Coach ethics](references/ethics.md)
- [Memory and privacy](references/memory.md)
- [Question methods and signal matching](references/tools.md)
- [Conversation workflow and output rules](references/workflow.md)
- [Relationship module](references/relationship.md)
- [Parent-child module](references/parent_child.md)
- [School mental health module](references/school_mental.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Conversational text or markdown, with optional local markdown memory notes when the host agent permits file access.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only skill; installed-skill memory is local-only according to the artifact, while the linked web version is a separate hosted service.]

## Skill Version(s):

2.5.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

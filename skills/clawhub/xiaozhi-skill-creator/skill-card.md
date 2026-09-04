## Description:

SKILL 编写工具 is a Chinese-language authoring guide for creating or revising learning skills with clear role, rule, memory, output, safety, and privacy boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and prompt-capable high-school learners use this skill to draft, revise, and diagnose Xiaozhi/OpenClaw learning skills while keeping platform conventions, memory fields, safety boundaries, and shared vocabulary consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crisis-support guidance includes mainland China emergency-channel assumptions that may not fit all user locations.

Mitigation: Localize crisis referral text and hotline information before deploying the skill for users outside mainland China.

Risk: The artifact references SECURITY_BASELINE.md, but that file is not included in the release evidence.

Mitigation: Obtain and review the publisher's SECURITY_BASELINE.md before relying on that baseline in deployment or review workflows.

Risk: The release license evidence conflicts with artifact frontmatter.

Mitigation: Confirm whether MIT-0 or MIT is the authoritative license before publishing the rendered card.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [Skill Templates Library](artifact/references/skill-templates-library.md)
- [Shared Vocabulary](artifact/shared/vocab.md)
- [Platform Conventions](artifact/shared/platform-conventions.md)
- [Crisis Exception](artifact/shared/crisis-exception.md)
- [Hint Ladder](artifact/shared/hint-ladder.md)
- [AI Item Check](artifact/shared/ai-item-check.md)
- [Grade Bands](artifact/shared/grade-bands.md)
- [DNA Profile Schema](artifact/shared/dna-profile.schema.json)
- [Handover Protocol Schema](artifact/shared/handover-protocol.schema.json)
- [External DNA Profile Schema URL](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with reusable prompt and skill templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-reviewed skill-writing guidance and template text; it does not execute tools or write student records.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

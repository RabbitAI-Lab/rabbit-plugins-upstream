## Description:

SKILL 编写工具 is a Chinese-language developer guide for writing education agent skills with clear role, rules, memory, output, safety, privacy, and troubleshooting boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and advanced high-school users use this skill to draft or revise education SKILL.md files, align them with shared vocabulary and schemas, and diagnose unstable skill behavior. It is not a subject tutor and does not generate exercises for students.

### Deployment Geography for Use:

Mainland China by default; other regions require localization of crisis contacts, curriculum assumptions, consent rules, and user-facing language before use.

## Known Risks and Mitigations:

Risk: The skill's templates and safety defaults assume a Chinese-language K12 setting with mainland China curriculum, consent, and crisis-contact conventions.

Mitigation: Before deployments outside mainland China, localize crisis contacts, curriculum assumptions, consent rules, and user-facing language.

Risk: Generated or revised skills may contain misleading guidance if copied without checking memory, sharing, reminder, and schema boundaries.

Mitigation: Review each generated SKILL.md against the bundled shared vocabulary, platform conventions, crisis protocols, and schemas before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [SKILL.md](artifact/SKILL.md)
- [Skill templates library](artifact/references/skill-templates-library.md)
- [Shared vocabulary](artifact/shared/vocab.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance and reusable SKILL.md template snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language K12 skill-authoring guidance; produces text specifications and templates rather than executable code.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

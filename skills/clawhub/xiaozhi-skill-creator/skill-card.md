## Description:

写一个新 SKILL 时用的编写工具，覆盖四层结构、边界声明、记忆字段、输出格式、安全与隐私边界、五步落地流程和常见问题诊断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and prompt-literate high school students use this skill to write or revise Chinese K12 learning skills with clear roles, rules, memory boundaries, output formats, and safety controls. It produces authoring guidance and templates rather than subject tutoring, exercise generation, or runtime actions.

### Deployment Geography for Use:

Mainland China by default; localize emergency contacts, curriculum assumptions, language defaults, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Mainland-China-specific emergency contacts, curriculum assumptions, language defaults, and minor-consent rules may not fit other regions.

Mitigation: Localize those items before relying on the templates outside Mainland China.

Risk: Skill drafts based on these templates can still contain unclear boundaries, unsafe retention rules, or unsuitable crisis wording if adopted without review.

Mitigation: Review generated drafts against the shared vocabulary, platform conventions, crisis protocol, and schemas before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Skill templates library](artifact/references/skill-templates-library.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Unified vocabulary](artifact/shared/vocab.md)
- [DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown guidance and structured text templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only authoring guidance; no hidden runtime, install, persistence, or execution behavior is indicated by security evidence.]

## Skill Version(s):

2.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

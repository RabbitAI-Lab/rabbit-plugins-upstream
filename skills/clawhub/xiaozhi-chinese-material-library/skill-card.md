## Description:

语文素材库 helps Chinese K12 students save writing materials with tags, retrieve 3-5 relevant items by theme, collect useful lines during reading or classical Chinese study after confirmation, and summarize confirmed usage counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to maintain a tagged Chinese writing-material library, retrieve suitable quotes or examples for composition topics, and record only user-confirmed material usage when profile sharing is enabled.

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: The bundled profile schema can validate broader persistent profile updates than the skill says it needs.

Mitigation: Limit runtime writeback to subjectExtensions.chinese.materialUsage and require the receiving profile service to enforce that field-level allowlist.

Risk: The skill handles student writing materials and usage counts, which can become persistent learning-profile data.

Mitigation: Require profileEnabled, crossSkillSharing, and per-use student confirmation before recording usage, and preserve view, correct, delete, pause, sharing-control, and export controls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [dna-profile.schema.json](shared/dna-profile.schema.json)
- [handover-protocol.schema.json](shared/handover-protocol.schema.json)
- [platform-conventions.md](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational Markdown with tagged material lists, retrieval suggestions, monthly summaries, and structured profile writeback guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose subject_profile_writeback updates for subjectExtensions.chinese.materialUsage only after user consent and confirmed material use.]

## Skill Version(s):

2.1.10 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

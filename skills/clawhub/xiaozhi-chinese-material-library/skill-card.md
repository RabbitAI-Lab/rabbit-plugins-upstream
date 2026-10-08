## Description:

Helps students save, tag, and retrieve Chinese writing materials, with optional usage tracking and monthly summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in mainland China's Chinese-language K–12 curriculum use this skill to collect and retrieve writing quotations and examples by topic. With consent, it can track confirmed use and provide a monthly summary.

### Deployment Geography for Use:

Mainland China; other regions require localizing safety contacts, curricula, and minors' consent rules.

## Known Risks and Mitigations:

Risk: Student writing materials and usage records may involve minors' data or be shared across skills or with parents without appropriate consent.

Mitigation: Confirm profile and sharing consent before use, honor pause, deletion, and parent-visibility controls, and check guardian requirements for minors.

Risk: Using mainland-China defaults outside the intended region may provide unsuitable safety contacts or consent handling.

Mitigation: Localize crisis contacts and minors' data practices before deployment outside mainland China.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Platform conventions](shared/platform-conventions.md)
- [Learning profile schema](shared/dna-profile.schema.json)
- [Crisis response guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tagged material lists, suggested uses, and on-request summaries; text export where supported.]

## Skill Version(s):

2.11.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

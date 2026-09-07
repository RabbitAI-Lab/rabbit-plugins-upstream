## Description:

SKILL 编写工具 helps developers and prompt-literate high school users write or revise learning-oriented SKILL files using a four-layer structure, safety and privacy boundaries, an implementation workflow, and diagnostic checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and prompt-literate high school users use this skill to draft or improve learning-focused SKILL files, including role, rules, memory fields, output behavior, safety boundaries, and handoff contracts. It is a developer reference skill and does not provide subject tutoring, generate exercises, or replace review of the generated SKILL.

### Deployment Geography for Use:

Global, with localization required for Chinese K12 assumptions and crisis resources outside China.

## Known Risks and Mitigations:

Risk: Templates are designed around Chinese K12 learning contexts, including crisis resources, consent rules, and school-stage assumptions.

Mitigation: Localize crisis contacts, consent requirements, and school-stage terminology before using generated skills in other regions.

Risk: Generated or revised SKILL text can still contain unclear boundaries, unsupported fields, or misleading guidance.

Mitigation: Review generated SKILL files against the bundled vocabulary, schemas, safety boundaries, and platform conventions before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Skill templates library](artifact/references/skill-templates-library.md)
- [Shared vocabulary](artifact/shared/vocab.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [AI item check](artifact/shared/ai-item-check.md)
- [Grade bands](artifact/shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured templates and inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only developer reference; no executable behavior.]

## Skill Version(s):

2.1.12 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

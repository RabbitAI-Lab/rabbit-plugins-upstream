## Description:

A developer guide for writing new learning SKILLs with a four-layer structure, safety and privacy boundaries, implementation steps, reusable templates, and troubleshooting checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SKILL authors, and advanced students use this skill to draft or revise learning-agent instructions, define memory and handoff contracts, preserve safety boundaries, and diagnose unstable skill behavior. It is a developer tool and does not provide subject tutoring, exercise generation, or student-facing learning support.

### Deployment Geography for Use:

Global, with localization review before student-facing deployment outside mainland China

## Known Risks and Mitigations:

Risk: Generated or revised learning skills may omit consent, privacy controls, or crisis-handling language.

Mitigation: Keep the bundled consent, data-control, and crisis-boundary sections in generated skills and review them before deployment.

Risk: A bundled handover schema has documented wording and logic inconsistencies.

Mitigation: Fix and review the handover schema wording and logic before using its templates in production workflows.

Risk: Safety contacts, curriculum assumptions, and minor-data consent defaults are designed around mainland China.

Mitigation: Localize crisis resources, curriculum references, and consent requirements before serving users in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [Skill templates library](references/skill-templates-library.md)
- [Vocabulary and thresholds](shared/vocab.md)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Hint ladder](shared/hint-ladder.md)
- [AI item check](shared/ai-item-check.md)
- [Grade bands](shared/grade-bands.md)
- [DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with prompt templates, checklists, schema references, and structured examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces authoring guidance and proposed skill text; it does not execute tools or store student data.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

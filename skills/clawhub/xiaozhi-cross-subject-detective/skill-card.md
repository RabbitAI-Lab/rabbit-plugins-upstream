## Description:

A Chinese K12 learning skill that guides students through a one-week cross-subject inquiry project, helping them choose a real-world theme, explore it from multiple disciplines, identify connections, and record project outcomes without doing single-subject homework or writing reports for them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students in upper primary, middle school, and high school use this skill to run a guided cross-disciplinary project around a real theme such as the Silk Road, climate change, or urbanization. Educators and learning platforms can use it to support inquiry prompts, hinting, project notes, and concept-graph writeback with student confirmation.

### Deployment Geography for Use:

Mainland China by default; localize crisis contacts, curriculum assumptions, and minor-consent requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can rely on long-term learning records and cross-skill sharing for project continuity.

Mitigation: Enable persistent records and cross-skill sharing only with appropriate student or guardian consent, and honor the built-in view, correct, delete, pause, sharing-control, and export commands.

Risk: The packaged safety and referral wording is written for mainland China and may include region-specific crisis contacts, curriculum assumptions, and consent defaults.

Mitigation: Before deployment outside mainland China, localize emergency contacts, curriculum alignment, and minor-consent handling; when the user's region is unknown, ask for it before giving region-specific help channels.

Risk: Ad hoc practice questions or project prompts could be incorrect or exceed the student's grade band.

Mitigation: Apply the included AI item self-check protocol and grade-band guidance before presenting generated questions or writing them into learning records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-cross-subject-detective)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Detective project template](references/detective-project-template.md)
- [Cross-subject connections template library](shared/cross-subject-connections.md)
- [Hint ladder](shared/hint-ladder.md)
- [Grade bands](shared/grade-bands.md)
- [AI item self-check protocol](shared/ai-item-check.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational text and Markdown project records with structured concept-graph and project writeback fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce student-confirmed project records, concept-graph nodes and edges, hint prompts, and handoff payloads; no executable code is shipped.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

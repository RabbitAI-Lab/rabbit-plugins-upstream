## Description:

AI literacy teaching agent for BNBU and broader education use cases that generates courseware, p5.js games, lesson packages, adaptive assessments, course recommendations, collaboration workflows, and WorkBuddy-oriented delivery plans through an eight-stage workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linix-2026](https://clawhub.ai/user/linix-2026)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, students, curriculum designers, and enterprise training teams use this skill to create AI-literacy teaching materials, interactive p5.js courseware and games, lesson-prep packages, assessments, learning plans, and collaboration workflows. It is especially tailored for BNBU/SAI scenarios and WorkBuddy delivery patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose saving generated teaching materials or reports to WorkBuddy cloud services such as IMA knowledge bases or Tencent Docs.

Mitigation: Require the agent and host to show the exact destination, account, document name, and data contents before any save or sync action.

Risk: The skill may propose sharing materials, reports, or collaboration links with recipients outside the immediate user context.

Mitigation: Confirm recipients, sharing scope, and revocation or deletion steps before sharing.

Risk: The skill may propose reminders, calendar events, memos, or scheduled workflows that persist beyond the current conversation.

Mitigation: Confirm timing, recurrence, notification target, and cancellation path before creating any scheduled or device-side item.

Risk: Generated assessments and learning reports may contain student performance details or other sensitive education data.

Mitigation: Review reports for personal or sensitive information and minimize what is written to shared cloud documents or knowledge bases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linix-2026/skills/ai-literacy-expert-v6)
- [Publisher profile](https://clawhub.ai/user/linix-2026)
- [Workflow orchestrator](references/workflow-orchestrator.md)
- [WorkBuddy adaptation guide](references/workbuddy-adaptation.md)
- [Automation operations guide](references/automation-ops.md)
- [BNBU/SAI module](references/module-e-bnbu-sai.md)
- [Assessment guide](references/assessment-guide.md)
- [Recommendation engine guide](references/recommendation-engine.md)
- [Commercial production standards](references/commercial-production-standards.md)
- [Example index](examples/INDEX.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated HTML, JavaScript, JSON, lesson-package outlines, assessment reports, and workflow plans when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose WorkBuddy cloud, document, sharing, calendar, reminder, memo, and device-side actions that require host/user confirmation before execution.]

## Skill Version(s):

6.0.0 (source: server release metadata and artifact meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

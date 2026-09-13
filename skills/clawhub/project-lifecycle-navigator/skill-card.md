## Description:

Audits project scope, drift, lifecycle decisions, repository health, and recent deliveries to produce bounded recommendations or handoffs without changing code or governance state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and project owners use this skill to decide whether to start, continue, narrow, pivot, archive, or stop a project. It supports new project intake, mid-project realignment, read-only repository health review, latest-delivery alignment, and owner-led target rebaseline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce ship, freeze, refactor, deletion, or coding-agent task-list recommendations that affect project direction.

Mitigation: Treat those recommendations as advice requiring explicit owner approval and a separate implementation workflow.

Risk: Repository audits may identify sensitive values or personal data in shipped artifacts.

Mitigation: Report only the affected path and exposure category, not the sensitive value itself.

Risk: A read-only review can be mistaken for final QA acceptance.

Mitigation: Keep Developer Complete, Verified, and Accepted separate, and require independent acceptance before treating a delivery as complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/englandtong/skills/project-lifecycle-navigator)
- [Quickstart](QUICKSTART.md)
- [Security](SECURITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown lifecycle reports, review findings, decision recommendations, and handoff plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only advisory output; implementation, governance changes, and QA acceptance require separate approval.]

## Skill Version(s):

2.1.1 (source: server release evidence and SKILL.md version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

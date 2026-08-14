## Description:

Automatically identifies wet clothing and abnormal excretion via visual AI and notifies caregivers for elderly, bedridden, infant, and other care scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and care-operations agents use this skill to analyze care images, videos, local files, or media URLs for damp clothing and abnormal excretion, then produce alerts, care suggestions, and report links. It also supports cloud-backed retrieval of historical incontinence alert reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive care images, videos, media URLs, and historical report queries are sent to Lifeemergence cloud endpoints.

Mitigation: Install and run only where patients, guardians, and caregivers understand and consent to the cloud data flow and where the publisher's privacy, retention, and access-control practices are acceptable.

Risk: The skill can silently create or reuse a persistent identity and store authentication tokens locally.

Mitigation: Use an isolated runtime or account, restrict access to local token storage, and review identity handling before deployment.

Risk: Visual AI care analysis may be inaccurate and is not a substitute for professional judgment or direct caregiver inspection.

Mitigation: Require human confirmation of alerts and care recommendations before taking clinical or caregiving action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)
- [Smart Incontinence Status Alert API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [markdown, json, shell commands, guidance]

**Output Format:** [Markdown reports, JSON analysis payloads, Markdown tables for report lists, and report URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified file path; cloud API responses include structured diagnosis fields, care warnings, suggestions, and report export links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

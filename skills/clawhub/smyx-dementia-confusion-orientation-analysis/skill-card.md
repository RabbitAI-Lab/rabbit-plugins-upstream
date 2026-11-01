## Description:

Analyzes camera footage, optionally with audio, for signs of confusion or disorientation in people with dementia and returns a structured report with orientation-support actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams in dementia care facilities and family caregivers can use the skill to review supplied recordings or query prior reports for observable signs of confusion and receive orientation-support actions. It supports care workflows and does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private care footage may still be uploaded when the environment-only option is used.

Mitigation: Before using private footage, verify a working environment-only mode, restrict service destinations, and confirm the provider's handling and deletion of recordings.

Risk: Account credentials may not be adequately protected.

Mitigation: Protect credentials and use separate accounts for separate users. Verify monitoring and alerting capabilities before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)
- [API interface and input guidance](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report with behavior findings, orientation-support actions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observable behavior and care-support actions; it does not provide medical diagnoses.]

## Skill Version(s):

1.0.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

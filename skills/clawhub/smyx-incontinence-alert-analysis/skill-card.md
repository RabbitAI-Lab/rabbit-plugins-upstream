## Description: <br>
Uses visual AI to identify wet clothing or abnormal excretion in care images or video, helping caregivers respond with timely alerts and structured reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers and care-operations agents use this skill to analyze uploaded or URL-based care images and video for wet-clothing or excretion alerts, generate structured care reports, and retrieve cloud-stored report history for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send sensitive patient, infant, or caregiver images and video URLs to the publisher's cloud service. <br>
Mitigation: Use only with explicit consent, authorized caregiver access, and confirmed retention, deletion, and access-control terms for real care data. <br>
Risk: The skill can create or reuse a local identity and persist local tokens. <br>
Mitigation: Deploy in a controlled environment, audit local identity and token storage, and rotate or remove credentials when access is no longer needed. <br>
Risk: Historical care reports are stored and retrieved from the cloud. <br>
Mitigation: Restrict report retrieval to authorized caregivers, define report retention expectations, and review access logging before production use. <br>
Risk: Visual analysis may be wrong or incomplete for care decisions. <br>
Mitigation: Treat alerts and reports as caregiver-support signals and require human confirmation before clinical or hygiene actions are delayed or escalated. <br>


## Reference(s): <br>
- [Incontinence Alert Analysis API Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports or JSON, with shell commands for execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local file or URL inputs, basic/standard/json detail levels, optional report output files, and cloud history listing.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

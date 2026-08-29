## Description:

Analyzes fixed-camera video and optional microphone input from dementia care or home settings to identify confusion or disorientation behaviors and produce structured orientation-soothing recommendations and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External care teams and developers use this skill to analyze dementia-care audio/video inputs for observable confusion, wandering, agitation, gaze drift, and repeated orientation questions, then return structured findings, escalation guidance, and report links. It is intended to support human-supervised care workflows, not to diagnose dementia or replace clinical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive dementia-care audio/video and may rely on cloud services, local identity reuse, remote account or token handling, and automated intervention flows.

Mitigation: Install only in an authorized care setting after confirming informed consent, visible notice, retention limits, backend endpoints, local identity and token storage, and human oversight.

Risk: Automated orientation soothing or escalation could be inappropriate if deployed without review in a care environment.

Mitigation: Disable or gate automated soothing and escalation until reviewed by responsible care staff, and require human supervision for operational use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recognition results, monitoring findings, soothing or escalation guidance, and historical report tables.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes monitoring images and videos for possible falls and provides structured findings and access to historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and home-safety teams use the skill to review possible falls in monitoring images or videos and consult past detection reports. Alerts are for triage and require human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring a person without consent may intrude on their privacy.

Mitigation: Obtain appropriate consent before using monitoring media.

Risk: Images, videos and report history are sent to configured cloud services.

Mitigation: Review the publisher's privacy, retention and authorization practices before sharing sensitive media.

Risk: The skill may silently create or reuse account identity and local tokens.

Mitigation: Confirm credential storage and account access controls with the publisher before installation.

Risk: A detection alert may be mistaken for a confirmed emergency assessment.

Mitigation: Verify suspected falls with a person and follow an emergency response procedure.

## Reference(s):

- [Fall-detection API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured detection results and report links; historical reports as a Markdown table or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved to a local file.]

## Skill Version(s):

1.0.16 (source: server release; bundled frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

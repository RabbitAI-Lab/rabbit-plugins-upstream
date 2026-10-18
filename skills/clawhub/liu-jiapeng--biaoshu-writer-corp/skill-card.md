## Description:

Helps prepare and review Chinese-language tender and bid documents through cloud-based interpretation, document generation, compliance checks, and similarity analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Bid teams and procurement professionals use the skill to interpret tender requirements, draft bid documents, identify compliance issues, and compare bids for similarity before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents are sent to the cloud service for processing.

Mitigation: Confirm permission to share each document and avoid uploading confidential material without approval.

Risk: Trial onboarding collects device characteristics and account setup may be less visible than expected.

Mitigation: Request explicit confirmation of the exact device fields sent before starting the trial.

Risk: An API key may be saved locally or exposed if pasted into a conversation.

Mitigation: Use a safer local secret mechanism where available, restrict access to stored credentials, and never repeat the key in responses.

Risk: Remote document URLs can lead to retrieval of untrusted content.

Mitigation: Use trusted document sources and review remote URLs before processing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/biaoshu-writer-corp)
- [Publisher profile](https://clawhub.ai/user/liu-jiapeng)
- [Usage guide](references/usage.md)
- [API overview](references/api.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files]

**Output Format:** [Text summaries, HTML or Word reports, DOCX bid documents, and JSON similarity results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bids may contain fields for the user to complete; document downloads can be time-limited.]

## Skill Version(s):

2.0.6 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

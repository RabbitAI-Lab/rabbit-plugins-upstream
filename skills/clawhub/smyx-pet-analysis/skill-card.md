## Description:

Analyzes pet videos or video URLs for possible health concerns and returns a structured health report with recommendations and a report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use the skill to assess cat, dog, or bird videos for possible health concerns and review health reports or past reports. Its findings are informational and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to a cloud service and may reveal household, location, or owner information.

Mitigation: Submit media only when cloud processing is acceptable; remove sensitive details from videos and URLs before sharing.

Risk: The skill silently creates or reuses a local identity and stores authentication tokens for later report access.

Mitigation: Review local credential storage and report-access behavior before installation; restrict access to the environment where tokens are stored.

Risk: Automated pet-health findings can be mistaken for a veterinary diagnosis.

Mitigation: Treat the report as informational and consult a veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Pet analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured text or JSON; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report link; analysis can optionally be saved to a file.]

## Skill Version(s):

999.999.1010 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

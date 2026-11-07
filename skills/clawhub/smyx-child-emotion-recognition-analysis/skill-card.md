## Description:

Analyzes images and video for signs of negative emotions in children and returns reports with findings and caregiver guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and service operators use the skill to analyze children's image or video footage for signs of distress and to retrieve historical analysis reports. Treat results as advisory and maintain direct adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised no-analysis option may still upload children's footage, and server-selection controls need fixing.

Mitigation: Wait until both controls are fixed before using private footage.

Risk: Remote account handling is insufficiently explained, and the provider's media retention, deletion, and access policies are not established by the package.

Mitigation: Confirm authorization for the provider to receive the media and create an account, and verify its retention, deletion, and access policies.

Risk: The local token database may expose credentials if inadequately protected.

Mitigation: Protect access to the local token database.

Risk: Advertised monitoring and parent alerts may not work as expected, and analysis cannot replace adult supervision.

Mitigation: Verify monitoring and alerts before relying on them, maintain adult supervision, and respond directly to urgent situations.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured analysis report; Markdown report listings; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can be saved to a file; historical report listings include links.]

## Skill Version(s):

1.0.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

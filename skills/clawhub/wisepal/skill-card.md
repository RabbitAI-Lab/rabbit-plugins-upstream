## Description:

Helps users lower US wireless, internet, and TV bills through free WisePal provider negotiations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wisepal](https://clawhub.ai/user/wisepal)

### License/Terms of Use:

MIT-0

## Use Case:

People in the United States use this skill to submit eligible bills to WisePal for free provider negotiations. The agent collects account details, confirms the information and terms with the user, and requests approval before provider calls may begin.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Bill, contact, and provider account details, including required PINs, are shared with WisePal.

Mitigation: Confirm the WisePal endpoint and terms before approval; keep PINs out of chat logs and share only the details needed for the requested negotiation.

Risk: Approving a submission can start real provider calls or schedule them for later.

Mitigation: Show validated details and terms, obtain explicit user consent, and proceed only when the user wants WisePal to contact providers on their behalf.

Risk: A lost local recovery credential can prevent continuation of an existing submission.

Mitigation: Keep the credential in private persistent storage and restore the original state for recovery rather than creating a duplicate submission.

## Reference(s):

- [WisePal ClawHub skill](https://clawhub.ai/wisepal/skills/wisepal)
- [WisePal homepage](https://wisepal.com)
- [Request schemas](artifact/references/request-schemas.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Conversational guidance and structured onboarding requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User confirmation and explicit consent are required before provider calls; savings are not guaranteed.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

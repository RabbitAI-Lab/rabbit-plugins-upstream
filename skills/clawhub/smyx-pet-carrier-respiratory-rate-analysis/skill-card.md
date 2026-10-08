## Description:

Analyzes pet carrier videos to estimate resting breathing rate, flag elevated rates, and provide monitoring reports without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and transport staff can submit a pet carrier video or URL to monitor breathing rate during travel and review alerts or past analysis reports. Results are informational and not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet carrier videos or video URLs are sent to a remote analysis service.

Mitigation: Confirm the recipient and obtain appropriate consent before submitting sensitive footage or URLs.

Risk: The skill silently creates or reuses an identity, stores authentication tokens locally, and can access cloud report history.

Mitigation: Restrict access to the local workspace and cloud account, and review who can access stored reports before use.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-carrier-respiratory-rate-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured breathing-rate report or Markdown history table, with optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes breathing-rate alerts and report links; historical reports are retrieved from the remote service.]

## Skill Version(s):

1.0.10 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

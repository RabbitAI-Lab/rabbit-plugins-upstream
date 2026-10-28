## Description:

Retrieves and summarizes Kuaishou (Kwai) work details, engagement metrics, and content information for research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content analysts use the skill to retrieve and review a Kuaishou work's title, author, publish time, and engagement metrics for content research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API lookups use the user's SocialDataX key and may consume credits.

Mitigation: Use an authorized key and check account or credit terms before repeated requests.

Risk: The CLI runs locally with the user's permissions, and this review does not cover future package releases.

Mitigation: Prefer a reviewed, pinned package version where possible and run it only with expected permissions.

Risk: Optional media downloads write files to the selected local destination.

Mitigation: Choose an explicit output directory and review media URLs before downloading.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-detail)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Structured JSON and factual natural-language summaries; optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only work-detail lookups; optional media saves to a user-selected local directory.]

## Skill Version(s):

0.1.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

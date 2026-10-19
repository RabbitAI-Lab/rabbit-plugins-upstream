## Description:

Creates competitor patent activity briefs that summarize recently published and granted patents, technical directions, and notable filings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts and business teams use this skill to track competitors' newly published and granted patents, spot technical trends, and prepare reviewable briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and supplied technical details are sent to the PatentMax service.

Mitigation: Do not include unpublished secrets or confidential invention details in searches unless sharing them with the service is approved.

Risk: A configurable service endpoint could redirect patent queries and API credentials to another destination.

Mitigation: Leave PATENTMAX_BASE_URL unset unless the alternative endpoint is explicitly trusted.

Risk: API calls may incur charges, and trial credentials or session data may be cached locally.

Mitigation: Confirm expected costs before running searches, protect PATENTMAX_API_KEY, and restrict access to local cached data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/competitor-patent-brief)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](artifact/references/api-reference.md)
- [Patent search workflow](artifact/references/search-workflow.md)

## Skill Output:

**Output Type(s):** [Text, CSV files]

**Output Format:** [UTF-8 CSV briefs and a conversational summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search scope, patent details, technical directions, notable findings, and a separate candidate-patent export.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Build source-attributed investor and fund shortlists from Crawlora's public PitchBook profiles and stored records while preserving gaps in coverage and fit evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Founders, fundraising teams, and their advisers use this skill to research and qualify potential investors and funds for a specified company and round, with citations and unresolved fit questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company, investor, fund, and search terms are sent to Crawlora using an API key.

Mitigation: Share only information appropriate for the service and keep the key out of prompts and logs.

Risk: Some searches charge credits per returned record.

Mitigation: Limit search scope and page sizes, and monitor credit usage.

Risk: Public profile coverage may be incomplete or outdated and cannot establish current investor appetite or available capital.

Mitigation: Attribute and date source evidence, preserve unknown criteria, and independently confirm material claims before outreach or decisions.

## Reference(s):

- [Investor Fit Research on ClawHub](https://clawhub.ai/crawlora-org/skills/investor-fit-research)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Source-attributed Markdown shortlist and fit matrix]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes firm and fund identities, supporting sources and dates, supported or unknown fit criteria, and follow-up questions; not investment advice or confirmation of available capital.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

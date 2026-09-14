## Description:

Researches software and SaaS products, business reputation, verified startup revenue, software reviews, BBB profiles, and Kickstarter campaigns through the Crawlora API, returning normalized JSON for due diligence and product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external researchers, and developers use this skill to evaluate software products, vendors, local businesses, startups, and crowdfunding campaigns before buying, partnering, or backing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and lookup parameters are sent to Crawlora.

Mitigation: Install only if that data sharing is acceptable; keep the API key in CRAWLORA_API_KEY and out of transcripts, screenshots, source control, and shared logs.

Risk: Private customer data or credentials could be exposed if included in lookup parameters.

Mitigation: Use public business, product, review, or campaign identifiers and avoid entering private customer or credential data.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/business-review-trust-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requested business, review, product, or campaign lookup parameters to Crawlora.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

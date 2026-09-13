## Description:

Researches software and SaaS products, business reputation, and crowdfunding campaigns through the Crawlora API, covering Product Hunt, Trustpilot, TrustMRR, Capterra, BBB, and Kickstarter and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill for vendor due diligence, product launch research, software review checks, verified revenue lookup, business reputation review, and crowdfunding campaign assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated API helper may allow broader Crawlora route or method use than the documented endpoint catalog describes.

Mitigation: Review the helper before installing in sensitive environments and restrict use to documented business-review endpoints.

Risk: Queries and request data are sent to Crawlora.

Mitigation: Use the skill only with inputs you are comfortable sending to Crawlora and avoid submitting confidential business information unless your account and data handling requirements allow it.

Risk: The helper uses an API key for authenticated requests.

Mitigation: Provide the key through CRAWLORA_API_KEY only, rotate it if exposed, and avoid sharing command output or logs that may reveal account usage.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/business-review-trust-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on Crawlora API responses and the requested source platform.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Search ads running across LinkedIn by keyword and/or advertiser company id, returning each ad's advertiser, ad copy, format, promoted label, thumbnail and a detail link, then open one ad in full with its media, headline, who paid for it and the advertiser's company URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and research analysts use this skill to query LinkedIn ad search and ad detail endpoints for competitor, paid-social, demand-generation, and ad-creative research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends LinkedIn ad search terms, company IDs, ad IDs, and the Scavio API key to Scavio.

Mitigation: Install and run it only when that data sharing is acceptable; keep SCAVIO_API_KEY in an environment variable or secret store.

Risk: Each LinkedIn ad endpoint is documented as costing 6 credits, so repeated calls can consume paid usage.

Mitigation: Use narrow queries, avoid unnecessary repeat calls, and monitor credit usage before large research runs.

Risk: LinkedIn CDN media links returned by the API can expire.

Mitigation: Fetch required media promptly instead of treating returned CDN URLs as durable storage links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/linkedin-ad-library-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [Scavio signup](https://dashboard.scavio.dev/sign-up?utm_source=clawhub&utm_medium=skill&utm_campaign=linkedin-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-ad-library-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. LinkedIn ad search and detail endpoints are documented as costing 6 credits each.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

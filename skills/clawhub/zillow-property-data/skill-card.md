## Description:

Search Zillow listings for sale, for rent or sold, pull one property in full with Zestimate and tax history, and read a real-estate agent's profile and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search Zillow listings, inspect detailed property records, retrieve agent profile reviews, and build real-estate comparisons or market monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and optional third-party SDK installation.

Mitigation: Keep SCAVIO_API_KEY in a secret store, rotate it when needed, use a virtual environment or project-local install for SDKs, and prefer direct HTTPS examples when package installation is not desired.

Risk: Real-estate data can be misread if estimates, filters, or agent reviews are presented as stronger evidence than they are.

Mitigation: Label Zestimate values as estimates, treat rental price filters as monthly rent, use only supported days-on-Zillow values, and keep agent reviews separate from property reviews.

## Reference(s):

- [Scavio Zillow Search Documentation](https://scavio.dev/docs/zillow-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=zillow-property-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=zillow-property-data)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/zillow-property-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and Python, JavaScript, or shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio Zillow endpoints return structured JSON and consume one credit per request.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

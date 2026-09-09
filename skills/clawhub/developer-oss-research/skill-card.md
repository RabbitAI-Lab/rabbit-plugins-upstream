## Description:

Researches public GitHub repositories, users, organizations, trending projects, and Chrome Web Store extensions through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to gather public GitHub and Chrome Web Store data for open-source due diligence, market research, trend tracking, and browser extension safety review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can send authenticated requests to paths beyond the documented GitHub and Chrome Web Store endpoints.

Mitigation: Run it only in a trusted environment and prefer a version that constrains calls to the documented endpoints.

Risk: Changing CRAWLORA_API_BASE can redirect authenticated requests away from the default Crawlora API.

Mitigation: Do not set CRAWLORA_API_BASE except during controlled testing with non-production credentials.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Keep CRAWLORA_API_KEY in the environment only and do not hardcode, pass in query strings, or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [developer-oss-research on ClawHub](https://clawhub.ai/tonywangcn/skills/developer-oss-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; list endpoints are paginated.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

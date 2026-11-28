## Description:

Deprecated compatibility skill for existing Desearch crawl integrations. It still extracts clean text or raw HTML through the legacy endpoint; use desearch-extract for new integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[desearch-ai](https://clawhub.ai/user/desearch-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining existing Desearch crawl integrations use this skill to retrieve a webpage as clean text or raw HTML. New integrations should use desearch-extract.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The full crawl URL and DESEARCH_API_KEY are sent to Desearch; URLs can contain account identifiers, tokens, or confidential query data.

Mitigation: Only submit URLs authorized for sharing with Desearch, and keep secrets and confidential information out of URLs.

Risk: The security scan had partial analysis because two local references were unresolved.

Mitigation: Review the skill and its documented network and environment-variable use before installing.

## Reference(s):

- [Desearch web crawl API reference](https://desearch.ai/docs/api-reference/get-web-crawl)
- [Desearch](https://desearch.ai)
- [Desearch Console](https://console.desearch.ai)

## Skill Output:

**Output Type(s):** [Text, HTML]

**Output Format:** [Plain text or raw HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the selected webpage representation to standard output.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

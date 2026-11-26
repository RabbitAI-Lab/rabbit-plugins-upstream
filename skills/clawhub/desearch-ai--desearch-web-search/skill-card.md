## Description:

Search the web and get SERP-style results with titles, URLs and snippets. Use this for general web queries when you need links to sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[desearch-ai](https://clawhub.ai/user/desearch-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search the web for general queries and review SERP-style titles, URLs, and snippets to find relevant sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, pagination offsets, and the API key are sent to Desearch; URLs or account identifiers included in a query are transmitted too.

Mitigation: Keep secrets and confidential information out of queries and submit only inputs you are authorized to share with Desearch.

Risk: The documented commands require outbound HTTPS and host execution access, and the skill's stated tool scope is not an enforced permission boundary.

Mitigation: Keep the API key protected and configure host execution and network access to match the intended use.

## Reference(s):

- [Desearch API Reference](https://desearch.ai/docs/api-reference/get-web)
- [Desearch](https://desearch.ai)
- [Desearch Console](https://console.desearch.ai)

## Skill Output:

**Output Type(s):** [JSON, Source links]

**Output Format:** [JSON search results printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 20 results per request; the count may vary, and the start offset supports pagination.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

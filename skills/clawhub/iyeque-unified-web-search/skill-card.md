## Description:

Searches the web and workspace files for bounded, source-labeled results with provenance information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can retrieve current web information or find relevant content in workspace memory and skills, with source-labeled results for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web search sends the query and Tavily API key to Tavily when network access is enabled.

Mitigation: Enable network search only for queries suitable for external disclosure; do not submit confidential prompts or secrets.

Risk: Local search reads matching content from workspace memory and skills when enabled.

Mitigation: Enable local search only when workspace content may be read, and review retrieved snippets before sharing them.

Risk: External search results can contain inaccurate information.

Mitigation: Verify important claims against their sources before relying on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iyeque/skills/iyeque-unified-web-search)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON search results with source labels, titles, scores, and snippets; warnings when a requested source is unavailable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 50 results per query; web results may include source URLs.]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Access live, normalized data from major social, search, maps, ecommerce, and web sources through AnyAPI when direct fetches or general web search are insufficient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kev1n](https://clawhub.ai/user/kev1n)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agents use this skill to discover AnyAPI SKUs, authenticate with AnyAPI, run paid or trial-backed data requests, and integrate AnyAPI results into research, monitoring, lead generation, and application workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install the AnyAPI CLI, store credentials, and register local tooling.

Mitigation: Review installation, credential storage, and MCP registration steps before running them in managed environments.

Risk: The skill can spend trial or wallet balance on paid third-party data requests.

Mitigation: Prefer explicit approval before paid calls, account connection, or actions that increase spending beyond the available trial.

Risk: Task inputs and bug reports may be sent to a third-party scraping and data API provider.

Mitigation: Avoid submitting secrets, sensitive personal data, or confidential business data unless the user has approved that disclosure.

Risk: Full API results may be saved locally by the AnyAPI CLI.

Mitigation: Handle saved result files as sensitive data and remove or restrict access to them when they contain private or proprietary information.

## Reference(s):

- [AnyAPI SDKs and direct HTTP](references/sdks.md)
- [AnyAPI CLI repository](https://github.com/getanyapi-com/cli)
- [AnyAPI hosted MCP endpoint](https://api.getanyapi.com/mcp)
- [AnyAPI documentation index](https://getanyapi.com/docs/llms.txt)
- [AnyAPI OpenAPI specification](https://api.getanyapi.com/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and integration code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local result files through the AnyAPI CLI and may reference billed request cost, balance, result IDs, and API schemas.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

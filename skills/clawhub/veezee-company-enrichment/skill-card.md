## Description:

Enrich a list of companies (names, domains, or LinkedIn URLs) with firmographic data like industry, employee count, headquarters, and founding year.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and research teams use this skill to enrich batches of company identifiers with LinkedIn firmographic data. It is suited for company lookup and batch research workflows where credit usage and unresolved identifiers need to be reported back to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company identifiers are sent to Veezee for enrichment.

Mitigation: Confirm the user is comfortable sharing the identifiers with Veezee before running enrichment.

Risk: The chosen MCP, SDK, or CLI setup stores a reusable Veezee API key.

Mitigation: Use an approved credential storage path and avoid exposing the key in logs, prompts, or shared output.

Risk: Large or paid batches can consume credits unexpectedly.

Mitigation: Check usage before a batch, set max_credits for calls where supported, and report total credits spent.

## Reference(s):

- [Company Enrichment Skill Page](https://clawhub.ai/veezee-build/skills/veezee-company-enrichment)
- [Veezee LinkedIn MCP Endpoint](https://mcp.veezee.io/linkedin)
- [Veezee MCP All Tools Endpoint](https://mcp.veezee.io/all)
- [Veezee API Key Mint Endpoint](https://api.veezee.io/v1/keys/mint)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown or text reports with company fields, invalid-input flags, closest matches, and credit totals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-company output should include name, industry, employee count, headquarters, website, founding year, and total credits spent.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

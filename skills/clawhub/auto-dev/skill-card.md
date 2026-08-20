## Description:

Auto.dev – Automotive Data helps agents work with Auto.dev APIs for vehicle data, VIN decoding, car listings, photos, specs, recalls, payments, interest rates, taxes, OEM build data, plate-to-VIN, CLI commands, MCP tools, and SDK methods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bryant22](https://clawhub.ai/user/bryant22)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Auto.dev automotive data, choose the available MCP, CLI, SDK, or direct API surface, and build vehicle-data workflows or applications. It supports agent guidance for authentication, endpoint selection, request parameters, pricing awareness, result formatting, and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill may send VINs, ZIP codes, credit scores, payment details, or license plates to Auto.dev.

Mitigation: Ask users for sensitive values instead of inferring them, send only the fields required for the chosen endpoint, and avoid persisting or unnecessarily repeating sensitive inputs.

Risk: Some Auto.dev endpoints and batch operations can incur per-call charges.

Mitigation: Estimate call counts and costs before batch work, warn users when paid endpoints are involved, and get explicit confirmation before high-cost operations.

Risk: Auto.dev API keys can be exposed if placed in client-side code or public files.

Mitigation: Prefer OAuth-backed CLI or MCP flows when available; for direct API use, keep AUTODEV_API_KEY in server-side environment configuration only.

Risk: Plate lookups can identify a specific vehicle and may involve regulated data.

Mitigation: Confirm a legitimate purpose before plate lookup, and do not run bulk plate lookups against plates the user did not provide.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bryant22/skills/auto-dev)
- [Auto.dev CLI, MCP, and SDK documentation](https://docs.auto.dev/v2/cli-mcp-sdk)
- [Auto.dev API documentation](https://docs.auto.dev/)
- [Auto.dev pricing](https://auto.dev/pricing)
- [V2 VIN API reference](artifact/v2-vin-apis.md)
- [V2 Listings API reference](artifact/v2-listings-api.md)
- [V2 Plate API reference](artifact/v2-plate-api.md)
- [Code patterns](artifact/code-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with inline command examples, API call guidance, code snippets, and optional CSV or JSON export instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide calls through MCP tools, CLI commands, SDK methods, or direct HTTP APIs depending on what is available to the agent.]

## Skill Version(s):

1.1.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

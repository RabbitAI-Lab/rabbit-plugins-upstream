## Description: <br>
x402lint guides agents through conformance scanning and discovery workflows for x402 seller origins, including free status and directory checks plus optional paid full reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect x402 seller origins, understand conformance categories, browse graded directory entries, and decide when to run paid scans or fetch cached reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional paid MCP tools use a wallet private key and funded USDC on Base. <br>
Mitigation: Use the free endpoints first, configure a dedicated low-balance wallet for paid tools, keep EVM_PRIVATE_KEY out of source control and logs, verify the x402lint-mcp package before funding it, and rotate the key if exposure is possible. <br>
Risk: x402lint grades measure protocol conformance, not safety, legitimacy, or endorsement of a scanned origin. <br>
Mitigation: Treat grades and directory branding as informational signals, perform independent diligence before paying a service, and remember that auto-collected directory text and links are unverified. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/jcislo/skills/x402lint) <br>
- [x402lint homepage](https://x402lint.dev) <br>
- [x402lint API](https://api.x402lint.dev) <br>
- [x402lint OpenAPI specification](https://api.x402lint.dev/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, text] <br>
**Output Format:** [Markdown guidance with shell command and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes free endpoint examples, paid x402 flow examples, MCP server configuration, and caveats for interpreting conformance grades.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

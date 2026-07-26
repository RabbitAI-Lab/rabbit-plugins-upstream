## Description: <br>
MCP Tools skill for AI agent commerce that helps agents search and compare products, prepare buyer-confirmed carts, create merchant-hosted checkout handoff links, and register or reuse hosted UCP identities without scraping or payment handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theagenttimes](https://clawhub.ai/user/theagenttimes) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent run structured shopping workflows through the UCP Gateway: product search, cart preparation after buyer confirmation, and merchant-hosted checkout handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts the remote UCP Gateway MCP service and creates local identity files. <br>
Mitigation: Install only when agent-assisted shopping through UCP Gateway is intended, keep the private key local, and review the generated ./.ucpgateway files. <br>
Risk: Cart or checkout actions could proceed without clear buyer intent. <br>
Mitigation: Require explicit buyer or operator confirmation before cart changes and final checkout handoff, and show totals, line items, messages, and warnings before proceeding. <br>
Risk: Payment or private buyer information could be mishandled. <br>
Mitigation: Do not collect payment credentials or invent buyer PII; direct the buyer to enter payment details only on the merchant-hosted checkout page. <br>


## Reference(s): <br>
- [UCP Gateway homepage](https://ucpg.ai/) <br>
- [UCP Gateway MCP endpoint](https://ucpg.ai/mcp) <br>
- [UCP Gateway registry](https://ucpg.ai/registry) <br>
- [UCP Gateway source repository](https://github.com/theagenttimes/ucp-gateway-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Shell commands, Configuration, JSON files] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local ./.ucpgateway identity files; checkout payment remains on merchant-hosted pages.] <br>

## Skill Version(s): <br>
0.2.4 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

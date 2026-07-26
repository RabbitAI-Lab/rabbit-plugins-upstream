## Description: <br>
Strykr Prism gives agents access to real-time financial data for crypto, stocks, forex, ETFs, commodities, DeFi, wallet, and market-intelligence requests through the PRISM API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and finance-focused agent builders use this skill to resolve asset identifiers, retrieve market prices and overviews, inspect token risks, and prepare PRISM API calls for financial analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market symbols, wallet addresses, contract addresses, and finance questions are sent to an external PRISM API provider. <br>
Mitigation: Use the skill only with a trusted PRISM provider, use a dedicated PRISM API key, and avoid querying wallets or addresses that should not be associated with the user. <br>
Risk: Broad finance activation phrases may send unrelated or over-broad text to the external service. <br>
Mitigation: Use explicit finance wording and review the intended query before invoking PRISM endpoints. <br>


## Reference(s): <br>
- [Strykr Prism on ClawHub](https://clawhub.ai/nextfrontierbuilds/skills/strykr-prism) <br>
- [Strykr PRISM API base URL](https://strykr-prism.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash and curl commands plus JSON API-response expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a PRISM API key for provider-backed API access.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata; artifact frontmatter says 1.1.1 and artifact skill.json says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

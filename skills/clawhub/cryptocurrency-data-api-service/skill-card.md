## Description: <br>
This skill helps an agent retrieve real-time cryptocurrency and DEX data, including tokens, liquidity pools, DEX listings, OHLCV history, transactions, search results, and ecosystem statistics through the XiaoBenYang API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and users of AI assistants can use this skill to answer cryptocurrency and DEX data questions by routing requests to supported tools for networks, DEXes, liquidity pools, token details, price history, transactions, search, stats, and batch token prices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a third-party XiaoBenYang service and requires an API key. <br>
Mitigation: Install and use it only when the publisher and service are trusted, and use a low-privilege key where possible. <br>
Risk: The security scan reports that the API key is stored in a local plaintext .env file. <br>
Mitigation: Keep the .env file out of source control and backups, restrict local file access, and rotate the key if it may have been exposed. <br>
Risk: The security scan notes confusing branding and a no-configuration claim despite required API-key setup. <br>
Mitigation: Confirm the intended upstream service and required setup before relying on returned crypto or DEX data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/cryptocurrency-data-api-service) <br>
- [XiaoBenYang API portal](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API Calls, guidance] <br>
**Output Format:** [Markdown summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-supplied network, DEX, pool, token, date, pagination, or search parameters depending on the selected tool.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
This skill helps agents run BrowserAct-powered Amazon product searches and return structured product listing data for market research, catalog discovery, and product monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phheng](https://clawhub.ai/user/phheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to collect Amazon product listings by keyword, brand, quantity, and language for market research, competitive monitoring, pricing intelligence, and catalog discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon search terms, brand filters, and product research context may be sent to BrowserAct. <br>
Mitigation: Confirm the search scope with the user before running, especially for confidential product, pricing, or market research. <br>
Risk: The BrowserAct API key could be exposed if pasted into chat or logs. <br>
Mitigation: Configure BROWSERACT_API_KEY through a local environment variable or approved secret manager, and do not ask the user to paste secrets into chat. <br>
Risk: The skill may provide insufficient user-facing control before external searches. <br>
Mitigation: Use explicit confirmation before executing searches that involve sensitive or business-critical inputs. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/phheng/skills/amazon-product-search-api-skill) <br>
- [Publisher profile](https://clawhub.ai/user/phheng) <br>
- [BrowserAct API key setup](https://www.browseract.com/reception/integrations) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text with status logs and structured product listing fields; may include JSON text returned by BrowserAct.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY. Sends search keywords, brand, result limit, and language to BrowserAct and polls until completion.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

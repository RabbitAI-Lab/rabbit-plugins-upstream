## Description: <br>
Crypto APIs (cryptoapis.io) helps agents search and read Crypto APIs market data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to query Crypto APIs market data through an OOMOL-connected account, including asset details, exchange rates, and supported asset listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crypto APIs lookups route through OOMOL and may consume account credits. <br>
Mitigation: Install and use the skill only for intended Crypto APIs market-data lookups, and review billing or credit status before retrying failed requests. <br>
Risk: First-time use requires installing the oo CLI and granting an OOMOL connection to Crypto APIs. <br>
Mitigation: Review the oo CLI installer and requested OOMOL connection permissions before setup, and do not repeat authentication or connection steps unless a command fails for that reason. <br>


## Reference(s): <br>
- [Crypto APIs homepage](https://cryptoapis.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-crypto-apis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before running read-only Crypto APIs actions; connector responses are JSON when actions execute.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

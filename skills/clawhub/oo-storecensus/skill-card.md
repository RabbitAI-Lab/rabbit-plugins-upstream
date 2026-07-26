## Description: <br>
StoreCensus helps agents search and read StoreCensus ecommerce intelligence through the OOMOL connector instead of calling the StoreCensus API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to retrieve website intelligence, search ecommerce stores, and browse Shopify app data from StoreCensus through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the oo CLI and an OOMOL-connected StoreCensus account, so setup, authentication, connection, or billing failures can block use. <br>
Mitigation: Run setup or connection steps only after the matching command failure, and verify the OOMOL account connection before retrying. <br>
Risk: Future StoreCensus connector actions labeled write or destructive could change or remove data. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before running any action labeled write or destructive. <br>


## Reference(s): <br>
- [ClawHub StoreCensus skill page](https://clawhub.ai/oomol/skills/oo-storecensus) <br>
- [StoreCensus homepage](https://www.storecensus.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

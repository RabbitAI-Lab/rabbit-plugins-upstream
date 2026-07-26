## Description: <br>
Operates Shopify Storefront through an OOMOL-connected account for reading storefront data and creating or modifying carts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, commerce operators, and their agents use this skill to inspect Shopify Storefront products, collections, shop metadata, and carts, and to create carts or add cart lines after confirming write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or modify Shopify Storefront carts through the connected OOMOL integration. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running cart-changing actions. <br>
Risk: The skill depends on an OOMOL account connection and may require one-time CLI installation or account connection steps. <br>
Mitigation: Run setup steps only when needed, and proceed only when the user trusts OOMOL and needs this connector. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shopify-storefront) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Shopify homepage](https://www.shopify.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

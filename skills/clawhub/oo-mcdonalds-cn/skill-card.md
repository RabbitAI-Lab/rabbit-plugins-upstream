## Description: <br>
McDonald's China helps agents search and read McDonald's China city, store, menu, and product information through the OOMOL mcdonalds_cn connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect McDonald's China locations, store business data, menus, and product details through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on OOMOL's oo CLI and an OOMOL-connected McDonald's China provider account. <br>
Mitigation: Install or authenticate the oo CLI only when needed, and connect the provider through the OOMOL account flow if an auth or connection error occurs. <br>
Risk: Using the connector can consume paid OOMOL credits. <br>
Mitigation: Review commands before running them and resolve HTTP 402 or insufficient-credit errors through OOMOL billing before retrying. <br>
Risk: Connector schemas and service behavior may change over time. <br>
Mitigation: Fetch the live action schema before constructing a payload and keep action use to the documented read-oriented lookups unless a future write action is explicitly confirmed. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/oomol/skills/oo-mcdonalds-cn) <br>
- [McDonald's China homepage](https://open.mcd.cn) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

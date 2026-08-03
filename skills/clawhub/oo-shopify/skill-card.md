## Description: <br>
Helps agents use the OOMOL Shopify connector and oo CLI to inspect schemas and run supported read-oriented Shopify REST Admin (Legacy) actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external Shopify operators use this skill to let an agent retrieve blog, article, page, tag, author, and shop configuration data from a connected Shopify REST Admin account through OOMOL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes a broad generic Shopify connector path that is not clearly limited to the documented read-only actions. <br>
Mitigation: Use only the listed read actions unless the user has separately confirmed the exact connector action, payload, and effect. <br>
Risk: A Shopify connection with write or delete permissions could allow higher-impact operations if a non-listed connector action is used. <br>
Mitigation: Review the skill before installation and confirm exact payloads and effects before any write or destructive action. <br>
Risk: First-time setup may install and authenticate the OOMOL CLI. <br>
Mitigation: Run setup steps only after a matching command failure and make authentication or connection changes explicit to the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shopify) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Shopify](https://www.shopify.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON data] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

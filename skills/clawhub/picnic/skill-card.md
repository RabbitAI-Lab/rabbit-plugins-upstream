## Description: <br>
Order groceries from Picnic supermarket - search products, manage cart, schedule delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mpociot](https://clawhub.ai/user/mpociot) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search Picnic products, manage a shopping cart, inspect delivery options, and prepare grocery orders for completion in the Picnic app. <br>

### Deployment Geography for Use: <br>
Germany and Netherlands <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses live Picnic account credentials and personal account data, including cart contents, delivery slots, delivery history, address, phone, and email. <br>
Mitigation: Install only when this account access is acceptable, avoid entering login commands in shared terminals or transcripts, and treat ~/.config/picnic/config.json as a sensitive credential file. <br>
Risk: The skill can modify the user's cart and select delivery slots. <br>
Mitigation: Confirm with the user before cart changes or slot selection, and complete final checkout or payment only in the Picnic app. <br>
Risk: debug.mjs reads the saved auth token and fetches delivery data. <br>
Mitigation: Do not run debug.mjs unless its credential and delivery-data access is understood and intended. <br>


## Reference(s): <br>
- [Picnic Grocery on ClawHub](https://clawhub.ai/mpociot/skills/picnic) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown guidance with shell commands; CLI commands return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Picnic account login and stores configuration in ~/.config/picnic/config.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

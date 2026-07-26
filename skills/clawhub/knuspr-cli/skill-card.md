## Description: <br>
Knuspr helps an agent manage grocery shopping on Knuspr.de through the bundled knuspr-cli for product search, cart updates, delivery slot reservations, shopping lists, order history, deals, favorites, and meal suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lars147](https://clawhub.ai/user/lars147) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to search Knuspr.de groceries, manage carts, lists, favorites, and delivery slots, review order history, and prepare shopping workflows while leaving final checkout to the user. <br>

### Deployment Geography for Use: <br>
Germany <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access a live Knuspr account and change carts, shopping lists, favorites, and delivery reservations. <br>
Mitigation: Use interactive login where possible, confirm cart/list/favorite/slot changes before execution, and personally review checkout in Knuspr before buying. <br>
Risk: Account credentials and session files may expose shopping account access if stored insecurely. <br>
Mitigation: Avoid passing passwords on the command line, protect or avoid ~/.knuspr_credentials.json, and keep session files private. <br>


## Reference(s): <br>
- [Full Command Reference](references/commands.md) <br>
- [Knuspr.de](https://www.knuspr.de) <br>
- [ClawHub Skill Page](https://clawhub.ai/lars147/skills/knuspr-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Often recommends --json for machine-readable CLI results; final checkout is left to the user.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

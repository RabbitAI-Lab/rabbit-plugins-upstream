## Description: <br>
Create, list, delete, and manage NEAR subaccounts with bulk distribution operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to manage NEAR subaccounts from the command line, including account creation, listing, deletion, and bulk token distribution from a configured master account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform NEAR account deletion and bulk token transfers without confirmation. <br>
Mitigation: Use only low-value or test accounts unless each delete or distribute action has been manually reviewed and explicitly approved. <br>
Risk: Bulk distribution depends on a user-provided JSON recipient list and amount. <br>
Mitigation: Inspect the JSON file, account IDs, and transfer amount before execution, and avoid automated runs until dry-run previews and confirmations are added. <br>
Risk: Shell commands are built from command-line arguments and environment values. <br>
Mitigation: Use trusted account names and controlled environment variables, and run the skill in a constrained shell environment. <br>


## Reference(s): <br>
- [NEAR CLI](https://docs.near.org/tools/near-cli) <br>
- [NEAR Subaccount docs](https://docs.near.org/concepts/account/subaccounts) <br>
- [ClawHub skill page](https://clawhub.ai/shaiss/skills/near-subaccount) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute NEAR CLI commands that create or delete accounts and transfer NEAR tokens when used by an agent with shell access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

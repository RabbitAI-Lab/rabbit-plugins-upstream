## Description: <br>
Austrian online grocery shopping via gurkerl.at. Use when user asks about "groceries", "Einkauf", "Lebensmittel bestellen", "Gurkerl", shopping cart, or wants to search/order food online in Austria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pasogott](https://clawhub.ai/user/pasogott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to search Gurkerl products, inspect order history, and manage shopping carts or lists for Austrian grocery shopping. <br>

### Deployment Geography for Use: <br>
Austria <br>

## Known Risks and Mitigations: <br>
Risk: The skill works with a live Gurkerl account and may expose credentials if a password is stored in plaintext environment files or shell profiles. <br>
Mitigation: Use the secure login flow with macOS Keychain when available, and avoid storing the Gurkerl password in ~/.env.local or shell profiles. <br>
Risk: Cart and shopping-list commands can add, remove, clear, create, or delete user shopping data. <br>
Mitigation: Review the proposed command before execution, especially destructive actions such as cart clear --force or list deletion. <br>


## Reference(s): <br>
- [gurkerl.at](https://gurkerl.at) <br>
- [ClawHub skill page](https://clawhub.ai/pasogott/skills/gurkerlcli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and CLI output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke gurkerlcli commands that return human-readable tables or JSON when the --json flag is used.] <br>

## Skill Version(s): <br>
0.1.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Manage Bring! shopping lists: view shared lists, add items, remove items, and handle list locale preferences. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[grewingm](https://clawhub.ai/user/grewingm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users and agents with Bring accounts use this skill to inspect shared grocery lists, add catalog-aware items, mark items as purchased, and manage default list and locale preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bring password and reusable authentication tokens are stored locally in plaintext under ~/.openclaw/bring. <br>
Mitigation: Install only on machines where local Bring credentials can be protected; restrict access to the config and token files and remove them when the skill is no longer used. <br>
Risk: The skill receives Bring account access and can read or modify shared shopping lists. <br>
Mitigation: Use only with Bring accounts and lists that the agent is allowed to manage, and consider using a unique Bring password for this integration. <br>


## Reference(s): <br>
- [Bring skill page](https://clawhub.ai/grewingm/skills/bring) <br>
- [Bring API Reference](references/api.md) <br>
- [bring-shopping package](https://github.com/foxriver76/node-bring-api) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and CLI JSON or text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require a configured Bring account and may read or update shared shopping-list data.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

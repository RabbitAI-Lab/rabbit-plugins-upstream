## Description: <br>
Manage Bring! shopping lists by helping an agent set up credentials, list available shopping lists, add or remove items, check items off, restore completed items, and run batch operations through the Bring API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maikimolto](https://clawhub.ai/user/maikimolto) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to manage Bring shopping lists from a local shell environment. It is suited for grocery-list setup and recurring list maintenance, including default-list selection, item lookup, adding, completing, uncompleting, and removing items. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a reusable Bring email and password locally, and the stored password can grant ongoing access to the Bring account from this machine. <br>
Mitigation: Prefer terminal credential entry, store the file with owner-only permissions, avoid password reuse, and treat ~/.config/bring/credentials.json as a secret. <br>
Risk: If a user chooses chat-based setup, their Bring credentials become part of the conversation history. <br>
Mitigation: Use the terminal setup path unless the user explicitly accepts the chat-history tradeoff after being warned. <br>
Risk: Remove and batch-remove commands delete items, and changes to shared Bring lists sync immediately to other devices. <br>
Mitigation: Confirm destructive actions with the user before execution, especially when the target list is shared. <br>
Risk: The skill relies on an unofficial Bring API flow that requires a direct Bring password and communicates with api.getbring.com. <br>
Mitigation: Make sure the user has a direct Bring password, not only Google or Apple sign-in, and keep network expectations limited to Bring's API. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maikimolto/skills/bring-list) <br>
- [Publisher profile](https://clawhub.ai/user/maikimolto) <br>
- [Bring website](https://getbring.com) <br>
- [Bring API endpoint](https://api.getbring.com/rest) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; writes local credential and token files when configured.] <br>

## Skill Version(s): <br>
1.2.7 (source: evidence.release.version and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

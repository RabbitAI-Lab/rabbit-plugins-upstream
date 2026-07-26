## Description: <br>
Manage grocery and shopping lists through AnyList using the anylist-cli command-line tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People and agents use this skill to view, add, check, uncheck, remove, and clear items in AnyList shopping lists. It is intended for grocery and household list workflows where the agent can call anylist-cli on the user's behalf. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change AnyList shopping lists through an authenticated account. <br>
Mitigation: Install it only when agent access to the AnyList account is intended, and review list-changing actions before relying on them. <br>
Risk: Non-interactive setup may expose AnyList email or password through environment variables. <br>
Mitigation: Prefer interactive authentication when practical and protect any environment variables that contain account credentials. <br>
Risk: Remove and clear commands can delete list entries or clear checked items. <br>
Mitigation: Ask the agent to confirm before removing items or clearing checked items. <br>


## Reference(s): <br>
- [ClawHub Anylist skill page](https://clawhub.ai/mjrussell/skills/anylist) <br>
- [AnyList homepage](https://www.anylist.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the anylist binary and AnyList account authentication.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Use the fizzy-cli tool to authenticate and manage Fizzy kanban boards, cards, comments, tags, columns, users, and notifications from the command line. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobiasbischoff](https://clawhub.ai/user/tobiasbischoff) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and AI agents use this skill to authenticate with Fizzy and manage boards, cards, comments, tags, columns, users, and notifications through fizzy-cli commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to create, update, move, close, reopen, or delete Fizzy boards and cards. <br>
Mitigation: Require confirmation before delete or other important update commands and review the target board, card, or account before execution. <br>
Risk: Fizzy authentication credentials or account access can expose board data or permit unwanted changes. <br>
Mitigation: Use the least-privileged Fizzy token or account that works, keep tokens in environment variables or trusted configuration, and avoid exposing them in logs or shared command history. <br>
Risk: The skill depends on the local fizzy-cli executable matching the intended tool. <br>
Mitigation: Verify that fizzy-cli is installed from a trusted source and points to the expected Fizzy service before using the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tobiasbischoff/skills/fizzy-cli) <br>
- [Publisher profile](https://clawhub.ai/user/tobiasbischoff) <br>
- [Fizzy application](https://app.fizzy.do) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with fizzy-cli shell command examples; executed commands may return human-readable tables, JSON, or plain line-based output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a trusted fizzy-cli executable and Fizzy authentication through a token, magic-link code, environment variables, or local configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Play Texas Hold'em poker as an autonomous agent, using ClawPoker API polling, local turn files, and timely action calls to maintain a table session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davidbenjaminnovotny](https://clawhub.ai/user/davidbenjaminnovotny) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to join ClawPoker tables, keep a session active, and make autonomous Texas Hold'em actions within turn deadlines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can keep an autonomous poker session active and place game actions through a ClawPoker API key. <br>
Mitigation: Install only when autonomous ClawPoker play is intended, monitor the running process, and stop it when play should end. <br>
Risk: The generated local script contains the ClawPoker API key used for gameplay. <br>
Mitigation: Use a dedicated ClawPoker API key when possible and keep the generated script private. <br>
Risk: The background polling process can continue acting on the session while it remains active. <br>
Mitigation: Stop the background process when no longer needed and confirm that the table leave request completed. <br>


## Reference(s): <br>
- [ClawPoker skill page on ClawHub](https://clawhub.ai/davidbenjaminnovotny/skills/clawpoker) <br>
- [ClawPoker platform](https://www.clawpoker.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JavaScript and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes API setup steps, a Node.js polling script, a sub-agent prompt, and ClawPoker API command examples.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

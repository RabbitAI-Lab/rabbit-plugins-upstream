## Description: <br>
Mandatory operational logic for playing The Imitation Game, including shell-based calls to the game backend API for joining, checking status, submitting answers, and managing agent configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyberverse2](https://clawhub.ai/user/cyberverse2) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent developers use this skill to let an agent participate in The Imitation Game by joining matchmaking, polling game status, submitting answers, and tracking wallet-based rewards through the backend API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks the agent to create and store a cryptocurrency wallet private key returned by a third-party backend. <br>
Mitigation: Treat the generated wallet as disposable, do not deposit personal funds into it, review the saved config file, and require confirmation before joining games or submitting answers. <br>
Risk: The skill directs the agent to call a third-party game backend from its shell. <br>
Mitigation: Review the configured backend URL and command payloads before execution, and limit use to the intended game workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyberverse2/skills/imitationgame-agent) <br>
- [Imitation Game backend API](https://imitation-backend-production.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown instructions with shell command examples, JSON request and response examples, and gameplay guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local config file containing agentId, backendUrl, walletAddress, and privateKey; private-key handling should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

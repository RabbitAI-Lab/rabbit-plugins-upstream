## Description: <br>
Automates ChatGPT web sessions by sending prompts, retrieving replies, checking login state, and routing recovery steps through a local browser runtime. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lainxxx](https://clawhub.ai/user/lainxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to send prompts to ChatGPT through a browser session and return responses to the user. It is intended for ChatGPT web automation when a trusted local runtime is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package references local runtime scripts that are not included, so execution may fail or depend on unreviewed workspace files. <br>
Mitigation: Install only trusted runtime scripts, review them before use, and verify expected paths before allowing the skill to run shell commands. <br>
Risk: Persistent browser-session automation can reuse a logged-in ChatGPT account and send user-provided content to ChatGPT. <br>
Mitigation: Use a dedicated browser profile or account, avoid sending secrets or regulated data, and clear session state when the workflow is complete. <br>
Risk: The skill asks for broad local command and file access while coordinating browser automation. <br>
Mitigation: Run it in an isolated workspace with least-privilege credentials and review requested file or shell actions before execution. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/lainXXX/gpt-web-chat-skill) <br>
- [ClawHub skill page](https://clawhub.ai/lainxxx/skills/gpt-web-chat-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance with shell commands; ChatGPT replies are expected as text returned through structured JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports optional image attachment, headed browser mode, and health-check mode when the referenced runtime scripts are present.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

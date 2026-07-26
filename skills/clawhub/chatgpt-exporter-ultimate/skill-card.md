## Description: <br>
Export all your ChatGPT conversations instantly - full context, timestamps, and metadata in seconds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[globalcaos](https://clawhub.ai/user/globalcaos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to export their ChatGPT conversation history, including project conversations, timestamps, metadata, and message content, into local backup files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create plaintext local copies of full ChatGPT conversation history, including sensitive prompts, responses, timestamps, IDs, and project conversations. <br>
Mitigation: Run it only when a complete local export is intentional, choose a private non-synced output directory, restrict file permissions, and avoid sharing raw exports. <br>
Risk: One export path accepts a live ChatGPT access token as a command-line argument. <br>
Mitigation: Prefer browser-session based execution where possible and avoid passing live access tokens on the command line. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/chatgpt-exporter-ultimate) <br>
- [Project repository linked by skill](https://github.com/globalcaos/clawdbot-moltbot-openclaw) <br>
- [ChatGPT](https://chatgpt.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript, TypeScript, shell commands, JSON exports, and Markdown conversation files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Exports may include full private ChatGPT conversation history, timestamps, conversation IDs, project conversations, and local summary files.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Store and retrieve memories using the SuperMemory API. Add content, search memories, and chat with your knowledge base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawdbot51-oss](https://clawhub.ai/user/clawdbot51-oss) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and end users use this skill to add personal knowledge to SuperMemory, search stored memories, and retrieve memory-backed answers through shell-command workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores user-provided memory content with a third-party memory API. <br>
Mitigation: Avoid storing passwords, API keys, regulated personal data, or confidential business information as memories; review SuperMemory retention and deletion behavior before use. <br>
Risk: The documentation includes an unsafe credential example that resembles a live API key. <br>
Mitigation: Do not use the documented key; configure a user-owned SUPERMEMORY_API_KEY and rotate any exposed credential before deployment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/clawdbot51-oss/skills/supermemory) <br>
- [SuperMemory documents API endpoint](https://api.supermemory.ai/v3/documents) <br>
- [SuperMemory search API endpoint](https://api.supermemory.ai/v3/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SUPERMEMORY_API_KEY and sends memory content and search queries to the SuperMemory API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

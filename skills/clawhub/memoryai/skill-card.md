## Description: <br>
MemoryAI provides long-term memory for AI agents so they can remember preferences, decisions, and context across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ch270035](https://clawhub.ai/user/ch270035) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use MemoryAI to let an agent store, recall, bootstrap, track, and save long-term context across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation messages, memory summaries, and profile data may be sent to a third-party memory service and retained as long-term memory. <br>
Mitigation: Use for non-sensitive work, avoid tracking secrets or regulated personal data, and confirm account-level export and delete controls before relying on long-term memory. <br>
Risk: The skill depends on an API key for the configured MemoryAI endpoint. <br>
Mitigation: Store HM_API_KEY securely, keep config.json free of committed secrets, and rotate the key regularly. <br>


## Reference(s): <br>
- [MemoryAI ClawHub Skill Page](https://clawhub.ai/ch270035/skills/memoryai) <br>
- [MemoryAI Service](https://memoryai.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text command output and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and HM_API_KEY; requests are sent to the configured HTTPS endpoint when commands are invoked.] <br>

## Skill Version(s): <br>
2.4.0 (source: frontmatter, changelog, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

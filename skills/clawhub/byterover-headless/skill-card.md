## Description: <br>
Query and curate a ByteRover knowledge base with the ByteRover CLI, including retrieval, context curation, and push/pull sync workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byteroverinc](https://clawhub.ai/user/byteroverinc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to manage project knowledge through ByteRover in headless automation, including querying stored context, curating new knowledge, and syncing context trees. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed if pasted into shared chats, logs, or persistent transcripts. <br>
Mitigation: Use a dedicated, revocable ByteRover API key and avoid pasting secrets into chat when possible. <br>
Risk: Curated project files or knowledge may be stored in ByteRover. <br>
Mitigation: Only curate files and context that are approved for storage in ByteRover. <br>
Risk: Push and pull operations sync local and remote context trees and can change the stored project knowledge state. <br>
Mitigation: Require explicit approval before push or pull actions. <br>


## Reference(s): <br>
- [ByteRover - Headless on ClawHub](https://clawhub.ai/byteroverinc/skills/byterover-headless) <br>
- [ByteRover publisher profile](https://clawhub.ai/user/byteroverinc) <br>
- [ByteRover API key settings](https://app.byterover.dev/settings/keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and expected JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the brv CLI and a ByteRover API key for authenticated setup.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

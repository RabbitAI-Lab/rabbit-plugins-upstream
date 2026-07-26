## Description: <br>
Control the IMA (ima.copilot) desktop application for AI search and private knowledge retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hyddd](https://clawhub.ai/user/hyddd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to launch Tencent IMA, run AI search queries, and optionally search an authorized private knowledge base through configured knowledge identifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automates Tencent IMA through a debugging port and can alter outgoing private-knowledge search requests. <br>
Mitigation: Use only with accounts and knowledge bases you are authorized to access, and review the behavior before installation or execution. <br>
Risk: Configured knowledge identifiers and private knowledge queries may expose sensitive enterprise or personal information if stored or run in the wrong environment. <br>
Mitigation: Protect saved knowledge ID configuration files and avoid running the skill in environments where private data could be unintentionally exposed. <br>


## Reference(s): <br>
- [Tencent IMA Skill on ClawHub](https://clawhub.ai/hyddd/skills/tencent-ima-skill) <br>
- [Clawdbot](https://github.com/clawdbot/clawdbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text search results with command-line and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS, the IMA.copilot desktop app, Python 3, websocket-client, and optional knowledge_id configuration for private knowledge base searches.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

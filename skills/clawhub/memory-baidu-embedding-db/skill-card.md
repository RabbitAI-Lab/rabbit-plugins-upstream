## Description: <br>
Semantic memory system that uses Baidu Embedding-V1 and SQLite to store and retrieve Clawdbot memories by meaning rather than keywords. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xqicxx](https://clawhub.ai/user/xqicxx) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Clawdbot operators use this skill to add semantic memory retrieval for preferences, conversation context, knowledge management, and related information lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Memory contents and search queries may be processed by Baidu for embeddings despite local-only privacy claims. <br>
Mitigation: Use only with data approved for Baidu processing, avoid sensitive memory content, and protect Baidu credentials outside shell history and logs. <br>
Risk: The release includes broad system-modifying scripts and instructions for disabling, restoring, cleaning up, changing permissions, and managing hooks. <br>
Mitigation: Do not run privileged disable, chmod, restore, cleanup, or hook scripts automatically; review each command and back up existing memory data and extensions first. <br>
Risk: Baidu API credentials may be exposed if copied into shell configuration, terminal output, or logs. <br>
Mitigation: Use a secret manager or protected environment injection, rotate credentials regularly, and avoid echoing credential values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xqicxx/skills/memory-baidu-embedding-db) <br>
- [Baidu Qianfan Console](https://console.bce.baidu.com/qianfan/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include setup steps, configuration values, memory API usage examples, and semantic search result handling.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

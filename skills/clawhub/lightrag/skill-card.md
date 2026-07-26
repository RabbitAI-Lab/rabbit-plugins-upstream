## Description: <br>
Searches and manages LightRAG knowledge bases through a configurable API client that supports multiple servers, query modes, context-aware writing, and direct information retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruslanlanket](https://clawhub.ai/user/ruslanlanket) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to configure LightRAG API servers, query knowledge bases in supported retrieval modes, and reuse returned context in writing or analysis tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles API keys and queries sent to configured LightRAG servers, which can expose credentials or sensitive prompts if the server or network path is not trusted. <br>
Mitigation: Use only trusted LightRAG servers and controlled network environments, and avoid sending sensitive queries unless the server and transport path are approved. <br>
Risk: The helper stores optional API keys in a local configuration file. <br>
Mitigation: Prefer environment variables or OS credential storage for real API keys, and ensure any local configuration file is readable only by the owning user. <br>
Risk: The query helper disables HTTPS certificate verification, weakening protection against network interception. <br>
Mitigation: Review or patch the helper so HTTPS certificate verification remains enabled before using it with real API keys or sensitive content. <br>


## Reference(s): <br>
- [LightRAG API Reference](references/API_DOCS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command usage and plain text query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return either a full response or context-only text from the configured LightRAG server.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

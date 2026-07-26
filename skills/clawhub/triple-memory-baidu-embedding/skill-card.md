## Description: <br>
Complete memory system combining Baidu Embedding auto-recall, Git-Notes structured memory, and file-based workspace search for persistent agent context, decisions, preferences, and tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xqicxx](https://clawhub.ai/user/xqicxx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to set up persistent multi-layer memory for conversation recall, structured decision tracking, workspace file search, and task or preference retention. Baidu embedding features require configured API credentials; otherwise the skill operates in degraded mode with Git-Notes and file-based memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill silently persists conversation data and may send text to Baidu when API credentials are configured. <br>
Mitigation: Review privacy and persistence behavior before installation, disable silent capture in shared or sensitive environments, and avoid storing secrets or sensitive personal or project data. <br>
Risk: The artifact makes local-only privacy claims that can be misleading when Baidu embedding calls are enabled. <br>
Mitigation: Document that embeddings may be processed by Baidu, and use degraded mode when external processing is not acceptable. <br>
Risk: Shell tooling sources workspace environment configuration before memory operations. <br>
Mitigation: Use only trusted environment files, prefer explicit exported credentials, and harden or disable environment-file sourcing before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xqicxx/skills/triple-memory-baidu-embedding) <br>
- [README.md](artifact/README.md) <br>
- [USAGE_EXAMPLES.md](artifact/USAGE_EXAMPLES.md) <br>
- [INTEGRATION_GUIDE.md](artifact/INTEGRATION_GUIDE.md) <br>
- [Baidu Qianfan console](https://console.bce.baidu.com/qianfan/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code] <br>
**Output Format:** [Markdown guidance with shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local memory files and call Baidu embedding services when credentials are configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

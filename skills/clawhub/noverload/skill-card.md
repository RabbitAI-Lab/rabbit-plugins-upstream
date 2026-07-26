## Description: <br>
Give your agent a searchable knowledge brain - semantic search, topic synthesis, and action tracking across your saved YouTube videos, articles, Reddit threads, X posts, and PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drewautomates](https://clawhub.ai/user/drewautomates) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an OpenClaw agent search, summarize, synthesize, and act on content saved in a Noverload knowledge library. It supports read-only retrieval by default and optional saving, tagging, and action updates when write access is enabled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the third-party Noverload service and noverload-mcp npm package. <br>
Mitigation: Install only when the publisher and package are trusted, and review the package source and behavior before deployment. <br>
Risk: The skill requires a personal access token for the user's Noverload account. <br>
Mitigation: Store the token securely, avoid committing or sharing it, and revoke or rotate it when access is no longer needed. <br>
Risk: Enabling write access can let the agent save URLs, add tags, mark items, or complete action items in the user's library. <br>
Mitigation: Keep readOnly:true unless write actions are specifically required and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drewautomates/skills/noverload) <br>
- [Noverload OpenClaw integration](https://noverload.com/openclaw) <br>
- [Noverload MCP documentation](https://noverload.com/docs/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and natural-language command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a Noverload access token; read-only mode is the default configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact Version section) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

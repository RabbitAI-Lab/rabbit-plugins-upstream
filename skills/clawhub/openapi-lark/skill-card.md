## Description: <br>
Syncs local or URL OpenAPI and Swagger specs into Feishu/Lark wiki and docx documentation trees with single-page, tag-tree, and per-endpoint layouts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to configure and run OpenAPI-to-Lark synchronization, preview generated API documentation, and diagnose Lark CLI authentication or scope issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide document-writing workflows that create, overwrite, move, or delete content in a Lark wiki/docx area. <br>
Mitigation: Use a dedicated project wiki node, start with dry-run, avoid shared wiki roots, and prefer reversible prune: move before considering prune: delete. <br>
Risk: Lark doc tokens and app secrets may grant broad access if stored directly in project configuration. <br>
Mitigation: Keep doc tokens and app credentials in environment variables and grant only the scopes needed for the selected workflow. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/leeguooooo/openapi-lark) <br>
- [Lark CLI](https://github.com/larksuite/cli) <br>
- [Team and CI sync guidance](https://github.com/leeguooooo/openapi-lark#-%E5%9B%A2%E9%98%9F--ci-%E5%90%8C%E6%AD%A5%E6%8E%A8%E8%8D%90%E5%A7%BF%E5%8A%BF) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with YAML and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to produce or update Lark wiki/docx API documentation through openapi-lark and lark-cli.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

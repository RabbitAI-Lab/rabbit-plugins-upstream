## Description: <br>
Access Jewish texts, commentaries, cross-references, and daily study materials from Sefaria through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abeperl](https://clawhub.ai/user/abeperl) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this MCP server to let MCP-compatible assistants search, read, and explore Jewish texts from Sefaria without an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text references and search queries are sent to Sefaria's public API. <br>
Mitigation: Use the server only when that disclosure is acceptable, and avoid sending sensitive private queries through it. <br>
Risk: Node package dependency updates can change the installed runtime code. <br>
Mitigation: For stricter supply-chain control, install in a way that honors the lockfile or review dependency updates before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/abeperl/skills/sefaria-mcp) <br>
- [npm Package](https://www.npmjs.com/package/sefaria-mcp-server) <br>
- [Sefaria](https://www.sefaria.org) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown] <br>
**Output Format:** [Markdown text returned through MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include Hebrew and English text, search snippets, references, links, calendar entries, and error messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

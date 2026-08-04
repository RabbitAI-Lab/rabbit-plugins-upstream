## Description: <br>
Access Artsonia student-art portfolios, comments, and fans via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to an Artsonia parent or fan account, review student artwork portfolios, manage comments and fans, and download artwork when authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP server receives access to an Artsonia parent or fan account. <br>
Mitigation: Install and register it only for accounts the user is authorized to access, and keep account credentials in private configuration. <br>
Risk: Downloaded artwork, sidecar JSON, comments, and teacher feedback can contain sensitive student data. <br>
Mitigation: Use a private destination folder, avoid shared or synced locations, remove exported files when no longer needed, and set include_private:false when private artwork should be excluded. <br>
Risk: Unpinned npx installs may change behavior across future package releases. <br>
Mitigation: Pin the npm package version when repeatable installs are required. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/artsonia-mcp) <br>
- [npm Package](https://www.npmjs.com/package/artsonia-mcp) <br>
- [Artifact-Declared Source Repository](https://github.com/chrischall/artsonia-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Files, JSON, Shell commands, Configuration] <br>
**Output Format:** [Natural-language responses, MCP tool results, setup snippets, downloaded image files, and optional JSON metadata sidecars] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save artwork images, comments, teacher feedback, indexes, and embedded metadata locally when download options are enabled.] <br>

## Skill Version(s): <br>
0.8.3 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

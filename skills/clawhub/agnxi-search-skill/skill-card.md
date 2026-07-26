## Description: <br>
The official search utility for Agnxi.com - The premier directory of AI Agent Tools, MCP Servers, and Skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[doanbactam](https://clawhub.ai/user/doanbactam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to search Agnxi for agent skills, MCP servers, and tool resources by keyword, then review returned links before installing or using them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes an outbound request to agnxi.com when searching. <br>
Mitigation: Use it only in environments where outbound access to Agnxi is expected and acceptable. <br>
Risk: Returned links may point to third-party tools, skills, or MCP servers that have not been reviewed. <br>
Mitigation: Review each returned resource before installation, execution, or delegation to an agent. <br>
Risk: The README example clone URL is a placeholder and does not prove package provenance. <br>
Mitigation: Use the server-resolved ClawHub listing and publisher profile when validating the release source. <br>
Risk: Passing untrusted search text through a shell wrapper could alter command behavior. <br>
Mitigation: Pass queries as process arguments rather than interpolating raw user text into shell commands. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/doanbactam/skills/agnxi-search-skill) <br>
- [Agnxi.com](https://agnxi.com) <br>
- [Agnxi sitemap](https://agnxi.com/sitemap.xml) <br>
- [OpenClaw standard](https://github.com/openclaw/clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text search status and a newline-delimited list of matching links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Limits displayed matches to the first 10 results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

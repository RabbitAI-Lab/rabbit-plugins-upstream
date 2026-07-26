## Description: <br>
一个MCP服务器，用于获取CPAN包的README内容、元数据和搜索功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to look up CPAN module README content, package metadata, dependencies, and package search results. It requires a XiaoBenYang API key before making remote CPAN lookup requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the XiaoBenYang API key in a local plaintext .env file. <br>
Mitigation: Use a separate low-privilege API key where possible and remove the .env entry when the skill is no longer needed. <br>
Risk: CPAN lookup parameters are sent to the XiaoBenYang remote service. <br>
Mitigation: Avoid placing sensitive or private text in package search queries or module lookup parameters. <br>
Risk: The security summary notes copied gaokao/school-service references, which may make the release harder to review. <br>
Mitigation: Review the skill description, configured tool IDs, and remote service behavior before installation or use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/cpan-package-info) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown summaries based on JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw CPAN lookup data with success status and message fields; requires an API key before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
MCP server providing profanity detection tools for AI assistants reviewing batches of user content, auditing comments for moderation reports, analyzing text before publishing, or adding content moderation capabilities to workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegdsks](https://clawhub.ai/user/thegdsks) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, moderators, and content teams use this MCP server with AI assistants to review batches of user content, audit comments for moderation reports, validate text before publishing, and support human-in-the-loop moderation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can track users and build moderation histories without documented storage, access, retention, or deletion controls. <br>
Mitigation: Confirm where message history is stored, who can access user profiles or high-risk lists, how long records are retained, and how incorrect or stale user data can be deleted before using tracking tools. <br>
Risk: The MCP server is installed from an npm package, creating supply-chain trust considerations. <br>
Mitigation: Install only when the npm package is trusted and the deployment has a real moderation need for the package's profiling and review capabilities. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thegdsks/skills/glin-profanity-mcp) <br>
- [glin-profanity-mcp npm package](https://www.npmjs.com/package/glin-profanity-mcp) <br>
- [glin-profanity core npm package](https://www.npmjs.com/package/glin-profanity) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [MCP tool responses and Markdown guidance with JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports batch checks up to 100 texts and corpus analysis up to 500 texts, per artifact documentation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and user changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

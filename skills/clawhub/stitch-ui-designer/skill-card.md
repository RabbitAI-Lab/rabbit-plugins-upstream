## Description: <br>
Design, preview, and generate UI code using Google Stitch via MCP, with preview-first iteration before exporting code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[a2mus](https://clawhub.ai/user/a2mus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and designers use this skill to generate UI concepts from text, review preview images, iterate on feedback, and export HTML/CSS after approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persistently configures a local MCP server that runs an unpinned external npm package in a Google Cloud-authenticated environment. <br>
Mitigation: Review before installing, prefer a dedicated least-privileged Google Cloud account and project, verify or pin stitch-mcp-auto where possible, and manually confirm configuration, authentication, project creation, and file write actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/a2mus/skills/stitch-ui-designer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Image previews, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, preview image results, and HTML/CSS code when approved] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npx and mcporter; uses a Stitch MCP server and may require Google Cloud authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

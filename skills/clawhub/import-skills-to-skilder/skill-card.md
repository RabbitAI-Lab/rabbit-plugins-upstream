## Description: <br>
Import the Agent Skills already present on this machine or in this repo into a Skilder workspace, so the whole team's agents can discover and run them from one governed endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skilder](https://clawhub.ai/user/skilder) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace administrators use this skill to inventory local Agent Skills, confirm which ones to import, and create corresponding Skilder skills and companion content in a workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local skill instructions and companion files may contain private content or secrets that should not be uploaded to a workspace. <br>
Mitigation: Review the inventory before import, skip private or secret-bearing files, and do not echo secret contents in the final report. <br>
Risk: The importer creates skills and companion content in a Skilder workspace through an authenticated admin session. <br>
Mitigation: Run it only from an account that should have workspace admin import authority and confirm the selected skills before creation. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/skilder/skills/import-skills-to-skilder) <br>
- [Skilder skills repository](https://github.com/skilder-ai/skills) <br>
- [Skilder MCP server](https://app.skilder.ai/mcp) <br>
- [Skilder workspace](https://app.skilder.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Markdown] <br>
**Output Format:** [Markdown summary with Skilder MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports imported skills, attached files, skipped files, duplicates, and errors.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

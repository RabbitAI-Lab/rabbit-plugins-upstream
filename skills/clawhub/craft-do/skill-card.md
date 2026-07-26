## Description: <br>
Integrates with Craft.do so agents can automate tasks, create and organize documents and folders, edit markdown content, and migrate Obsidian vaults through the Craft REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atomtanstudio](https://clawhub.ai/user/atomtanstudio) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation builders use this skill to interact with Craft.do workspaces, migrate Obsidian vault content, and manage Craft tasks, folders, and documents through API-oriented shell workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload selected Obsidian notes and other markdown content to Craft. <br>
Mitigation: Use a non-critical Craft space or verified backup first, and confirm the vault path and files selected before migration. <br>
Risk: Craft API credentials allow workspace-changing API calls. <br>
Mitigation: Store CRAFT_API_KEY securely, verify CRAFT_ENDPOINT before running commands, and avoid exposing credentials in logs or shared shell history. <br>
Risk: cleanup-craft.sh is designed to remove all user-created folders and move all documents to trash. <br>
Mitigation: Run cleanup only after confirming the target workspace and keeping a recoverable backup; avoid using it on important spaces unless that deletion is intentional. <br>


## Reference(s): <br>
- [Craft API Documentation](https://craft.do/api) <br>
- [ClawHub Skill Page](https://clawhub.ai/atomtanstudio/skills/craft-do) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and shell script workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided Craft API key, Craft API endpoint, and optional Obsidian vault path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

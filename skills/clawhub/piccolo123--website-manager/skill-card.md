## Description: <br>
Cross-platform URL collection and knowledge management for saving, organizing, searching, and sharing web resources through an agent-operated hosted service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[piccolo123](https://clawhub.ai/user/piccolo123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to save URLs or notes, organize them into personal or shared categories, search prior saved resources, and deliver card-based collections through a magic link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-create an account on ai.ocean94.com and upload saved URLs, notes, categories, and shared collection data to that hosted service. <br>
Mitigation: Get clear user permission before first use, explain that data is stored on ai.ocean94.com, and point users to the hosted service for viewing, managing, and deleting their data. <br>
Risk: The skill persists a reusable local token in a .token file. <br>
Mitigation: Protect the token file with restrictive permissions, avoid exposing it in logs or shared workspaces, and rotate credentials if the token may have been disclosed. <br>
Risk: Shared category operations and invite links can affect other collaborators or expose curated collections. <br>
Mitigation: Confirm with the user before generating magic links, creating invite links, or modifying shared categories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/piccolo123/skills/website-manager) <br>
- [Publisher profile](https://clawhub.ai/user/piccolo123) <br>
- [Hosted URL Manager service](https://ai.ocean94.com) <br>
- [User Agreement](https://ai.ocean94.com/terms.html) <br>
- [Privacy Policy](https://ai.ocean94.com/privacy.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and network access to ai.ocean94.com; commands can emit machine-readable JSON with --json.] <br>

## Skill Version(s): <br>
2.6.2 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

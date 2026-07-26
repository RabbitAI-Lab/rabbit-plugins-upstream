## Description: <br>
Search, list, and manage Raindrop.io bookmarks via CLI, including reading saved links and collections and writing changes such as add, delete, move, update, and bulk move operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[velvet-shark](https://clawhub.ai/user/velvet-shark) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent search, inspect, organize, and update a Raindrop.io bookmark library from a command-line workflow. It is suited for bookmark retrieval, collection browsing, tagging, collection moves, and controlled bulk organization tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete bookmarks and perform bulk moves in the user's Raindrop.io account. <br>
Mitigation: Confirm bookmark IDs, collection targets, and bulk ID lists before running delete, update, move, or bulk-move commands. <br>
Risk: The skill can use a local token file at ~/.config/raindrop.env if an environment token is not already set. <br>
Mitigation: Prefer a trusted environment variable or runtime --token value, and keep ~/.config/raindrop.env private with restrictive permissions if used. <br>


## Reference(s): <br>
- [Raindrop.io API documentation](https://developer.raindrop.io/) <br>
- [Raindrop.io integrations settings](https://app.raindrop.io/settings/integrations) <br>
- [ClawHub skill page](https://clawhub.ai/velvet-shark/skills/raindrop) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, jq, bc, and a Raindrop.io API token supplied through RAINDROP_TOKEN, --token, or ~/.config/raindrop.env.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

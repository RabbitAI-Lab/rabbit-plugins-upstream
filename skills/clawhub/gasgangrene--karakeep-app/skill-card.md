## Description: <br>
Official skill for how to use karakeep (the bookmark manager) and interact with it programmatically. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate a Karakeep bookmark manager instance through the CLI, including adding, organizing, searching, updating, and deleting bookmarks, lists, and tags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Karakeep API key, which could expose account access if handled insecurely. <br>
Mitigation: Use environment variables or a secret manager, and avoid passing API keys directly on the command line. <br>
Risk: CLI commands can modify or delete Karakeep bookmarks and lists when the user directs those actions. <br>
Mitigation: Require explicit user confirmation before destructive commands such as deleting bookmarks or lists. <br>


## Reference(s): <br>
- [Karakeep homepage](https://karakeep.app) <br>
- [Karakeep documentation](https://docs.karakeep.app) <br>
- [Karakeep repository](https://github.com/karakeep-app/karakeep) <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/karakeep-app) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CLI commands that return JSON when --json is requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

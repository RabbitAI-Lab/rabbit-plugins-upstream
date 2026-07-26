## Description: <br>
Manage bookmarks and links in a Karakeep instance by saving links, listing recent bookmarks, and searching a user's collection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jayphen](https://clawhub.ai/user/jayphen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Karakeep users use this skill to configure access to a Karakeep instance, save links or text as bookmarks, list recent bookmarks, and search an existing bookmark collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and uses a Karakeep API key locally in plaintext when the login command is used. <br>
Mitigation: Use a least-privilege or revocable API key, verify the configured instance URL before use, and restrict permissions on ~/.config/karakeep/config.json. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jayphen/skills/karakeep) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Plain text with shell commands and CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv, network access to the configured Karakeep instance, and a Karakeep API key supplied through environment variables or local configuration.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

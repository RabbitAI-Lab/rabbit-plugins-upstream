## Description: <br>
CLI for AI agents to lookup Harry Potter universe info for their humans. Uses HP-API. No auth required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let agents run simple Harry Potter universe lookups for characters, Hogwarts roles, houses, and spells through HP-API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lookup terms may be sent to HP-API when the skill runs. <br>
Mitigation: Use the skill for public Harry Potter lookups only and avoid entering sensitive or private text as queries. <br>
Risk: The README references an external GitHub repository whose executable scripts were not included in the reviewed artifact. <br>
Mitigation: Inspect any externally fetched executable scripts before installation or execution. <br>


## Reference(s): <br>
- [HP-API](https://hp-api.onrender.com) <br>
- [Harrypotter on ClawHub](https://clawhub.ai/jeffaf/skills/harrypotter) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text CLI output with concise character, house, and spell records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, and jq; calls HP-API without authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

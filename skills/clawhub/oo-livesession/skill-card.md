## Description: <br>
LiveSession connector skill for listing session replay data through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect LiveSession connector schemas and list session replay data through an authenticated OOMOL connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session replay metadata can expose customer or visitor activity. <br>
Mitigation: Install and use the skill only in workspaces where access to LiveSession replay listings is appropriate. <br>
Risk: Connector commands run through the user's OOMOL-connected account. <br>
Mitigation: Inspect the live connector schema before constructing payloads and keep execution to the documented read-only list_sessions action unless future write or destructive actions are explicitly confirmed. <br>


## Reference(s): <br>
- [ClawHub LiveSession Skill](https://clawhub.ai/oomol/skills/oo-livesession) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [LiveSession Homepage](https://livesession.io) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; current documented action is read-only list_sessions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

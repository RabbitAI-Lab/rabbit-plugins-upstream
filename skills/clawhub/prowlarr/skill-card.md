## Description: <br>
Search indexers and manage Prowlarr through API-backed commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmagar](https://clawhub.ai/user/jmagar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and operators with a configured Prowlarr instance use this skill to search torrent and Usenet indexers, inspect health and status, manage indexers, and sync indexer changes to connected apps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a Prowlarr API key for the configured instance. <br>
Mitigation: Protect the credentials file and prefer a limited or dedicated API key when available. <br>
Risk: Delete, enable, disable, test, and sync commands are real Prowlarr administrative actions. <br>
Mitigation: Require clear user confirmation before delete or sync commands and verify indexer IDs before enable, disable, or delete actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jmagar/skills/prowlarr) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Prowlarr URL and API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

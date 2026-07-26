## Description: <br>
Confluence enables agents to read, search, create, and update Confluence content through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and external users use this skill to retrieve Confluence pages, list spaces, search content with CQL, and create or update pages after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update Confluence pages through the connected account. <br>
Mitigation: Confirm the exact write payload and intended effect with the user before running create or update actions. <br>
Risk: The skill can read Confluence content available to the connected account. <br>
Mitigation: Install it only when OOMOL and the connected Confluence account are trusted for the content the agent may access. <br>
Risk: Actions may fail when authentication, connector scopes, credentials, or account billing are not ready. <br>
Mitigation: Use the documented setup fallback only after an action fails for the matching auth, connection, scope, credential, or billing reason. <br>


## Reference(s): <br>
- [ClawHub Confluence skill page](https://clawhub.ai/oomol/skills/oo-confluence) <br>
- [Confluence homepage](https://www.atlassian.com/software/confluence) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI installation guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read actions can run directly; write actions require user confirmation of the exact payload and effect.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

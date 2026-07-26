## Description: <br>
Manage Things 3 tasks through Things Cloud using the maintained things-cloud-sdk CLI and MCP server, with dry-run safety for agent writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pdurlej](https://clawhub.ai/user/pdurlej) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People who manage Things 3 tasks use this skill to let an agent inspect task lists, search task data, and prepare safe task updates through Things Cloud. It is suited for MCP-capable agent hosts and CLI workflows that need credential-aware read and write guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Third-party Things Cloud tooling receives access to the user's Things Cloud account. <br>
Mitigation: Install only when the publisher and things-cloud-sdk tooling are trusted for the account being used. <br>
Risk: Credentials could be exposed if passwords or tokens are stored in repositories or skill files. <br>
Mitigation: Prefer THINGS_TOKEN over THINGS_PASSWORD where possible and keep Things Cloud credentials out of repositories. <br>
Risk: Agent-generated writes could change user-visible tasks incorrectly. <br>
Mitigation: Use dry-run previews, summarize the planned change, and get user confirmation before running non-dry-run writes. <br>


## Reference(s): <br>
- [things-cloud-sdk](https://github.com/pdurlej/things-cloud-sdk) <br>
- [ClawHub skill page](https://clawhub.ai/pdurlej/skills/things-cloud) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Things Cloud MCP tools or CLI commands and previews writes with dry-run before execution.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

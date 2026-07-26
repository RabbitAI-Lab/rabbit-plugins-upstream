## Description: <br>
Use Factory AI's droid CLI for software engineering tasks, including interactive work, non-interactive exec mode, MCP servers, and plugins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mitchellbernstein](https://clawhub.ai/user/mitchellbernstein) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and software engineering agents use this skill to operate Factory AI's droid CLI for building features, debugging, refactoring, reviewing code, managing MCP servers or plugins, and running deployment-related tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The droid CLI can make code changes, run deployment-related tasks, create commits or PRs, and add plugins or MCP servers. <br>
Mitigation: Require human review before commits, PRs, deployments, plugin installs, MCP server changes, or other actions that affect repositories or infrastructure. <br>
Risk: The skill depends on a powerful third-party binary and account connection. <br>
Mitigation: Install only from a trusted Factory Droid source, verify the binary version before use, and confirm the account or organization access scope. <br>
Risk: The documented --force option can auto-apply changes without confirmation. <br>
Mitigation: Avoid --force unless automatic changes are explicitly intended and the working tree can be reviewed or reverted. <br>
Risk: Session-based memory and organization-wide code understanding may retain or expose sensitive context. <br>
Mitigation: Confirm how Factory scopes code access and how session memory is cleared or isolated before using the skill with sensitive repositories. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with code and shell command snippets; optional JSON when droid exec --json is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill delegates outputs to the third-party droid CLI and may produce code changes, command guidance, review findings, configuration steps, or deployment instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

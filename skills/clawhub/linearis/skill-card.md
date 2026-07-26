## Description: <br>
Linear.app CLI for issue tracking that helps agents list, create, update, and search Linear issues, comments, documents, cycles, and projects with JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whoisnnamdi](https://clawhub.ai/user/whoisnnamdi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Linearis to let an agent inspect and manage Linear issues, comments, documents, projects, cycles, teams, users, and file embeds through a JSON-emitting CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Linear API tokens can be exposed through command-line flags, shell history, logs, or unprotected token files. <br>
Mitigation: Treat the Linear API token as a secret, prefer protected environment or file-based configuration, avoid command-line token flags where logs may capture them, and protect any token file. <br>
Risk: Agent-executed commands can create, update, or delete Linear records and upload or download files in a live workspace. <br>
Mitigation: Require explicit approval before mutating Linear data or transferring files, and review command arguments and JSON output before continuing. <br>


## Reference(s): <br>
- [Linearis ClawHub page](https://clawhub.ai/whoisnnamdi/skills/linearis) <br>
- [Linearis documentation](https://github.com/czottmann/linearis) <br>
- [Linearis blog post](https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html) <br>
- [Linear](https://linear.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; the referenced CLI returns JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the linearis CLI and a Linear API token.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

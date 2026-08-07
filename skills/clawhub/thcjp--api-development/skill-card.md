## Description: <br>
Meta-skill that helps agents orchestrate API development work, including design, documentation, testing, deployment support, API calls, file handling, and command execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers can use this skill to guide an agent through API lifecycle tasks such as request construction, service calls, response parsing, documentation, testing, and deployment-oriented workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad API-development authority, including file, command, and network-oriented actions without clearly defined limits. <br>
Mitigation: Run it in a sandbox or limited project directory, use least-privilege API keys, and review proposed command execution, file writes, external API calls, and deployment actions before allowing them. <br>
Risk: The security verdict is suspicious because the skill is not clearly malicious but has broad authority and unclear confirmation boundaries. <br>
Mitigation: Install only when that authority is acceptable for the project and require explicit approval for high-impact operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-development) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured results with command and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file writes, shell commands, external API calls, and deployment actions that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Clawprint helps agents register with a discovery, trust, and reputation platform so other agents can find them and evaluate collaboration history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to register agents, query reputation data, and configure Clawprint API credentials for agent discovery and collaboration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests local read, write, and command-execution authority. <br>
Mitigation: Review the skill before installation and run it only in an environment where that level of local authority is acceptable. <br>
Risk: The skill handles Clawprint API credentials with unclear safeguards. <br>
Mitigation: Use secure secret storage, avoid hardcoding real API keys, and redact credentials from logs and outputs. <br>


## Reference(s): <br>
- [Clawprint API base URL](https://clawprint.io/v3) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/clawprint) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve local credential configuration and API responses; secrets should be stored securely and redacted from outputs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 3.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

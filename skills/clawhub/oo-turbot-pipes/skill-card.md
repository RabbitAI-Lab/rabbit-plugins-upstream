## Description: <br>
This skill supports searching and reading data through the Turbot Pipes connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect the Turbot Pipes connector schema and run SQL queries through an OOMOL-connected account. It is intended for read/query workflows that return Turbot Pipes rows and query metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may run SQL queries against sensitive Turbot Pipes datasets. <br>
Mitigation: Review SQL queries before execution and approve access to sensitive datasets deliberately. <br>
Risk: Setup, authentication, or account-connection commands can affect the user's OOMOL account state. <br>
Mitigation: Run CLI installation, login, and Turbot Pipes connection steps only after an auth or connection failure and with explicit user approval. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-turbot-pipes) <br>
- [Turbot Pipes Homepage](https://turbot.com/pipes) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses may include JSON data and execution metadata from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

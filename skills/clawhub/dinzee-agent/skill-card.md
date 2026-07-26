## Description: <br>
DinzeeAgent helps agents discover and call cross-border e-commerce data tools through the Dinzee Gateway while managing authentication, billing, and remote business-skill installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yefeng311](https://clawhub.ai/user/yefeng311) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, e-commerce operators, and agent developers use DinzeeAgent to discover available data providers, call Dinzee-mediated MCP tools for product and market research, and install or update Dinzee business skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install or update executable skill packages from the Dinzee gateway into a local agent skill directory. <br>
Mitigation: Install or sync packages only when the Dinzee publisher and gateway are trusted, and confirm which skills will be written before running install, update, or sync commands. <br>
Risk: Gateway use depends on a Dinzee user token that may be stored locally for repeated calls. <br>
Mitigation: Use a per-user token, keep the credential file permission-restricted, and know how to revoke or rotate the token before relying on the skill. <br>


## Reference(s): <br>
- [DinzeeAgent ClawHub listing](https://clawhub.ai/yefeng311/skills/dinzee-agent) <br>
- [Dinzee Gateway](https://gateway.dinzee.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include gateway request IDs, billing summaries, and synthesized e-commerce analysis.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

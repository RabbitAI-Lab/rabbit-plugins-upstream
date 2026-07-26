## Description: <br>
Helps agents inspect MongoDB Atlas projects and clusters through the OOMOL MongoDB Atlas Administration connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to discover MongoDB Atlas projects and inspect clusters visible to their connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad MongoDB Atlas prompts may route to this skill even when the user intended a narrower task. <br>
Mitigation: Use specific requests and review any proposed command before allowing the agent to run it. <br>
Risk: The skill operates through connected MongoDB Atlas credentials and can read project and cluster information available to that connection. <br>
Mitigation: Use least-privilege Atlas credentials and review requested project IDs, cluster names, and returned information before relying on the output. <br>


## Reference(s): <br>
- [MongoDB Atlas Administration on ClawHub](https://clawhub.ai/oomol/skills/oo-mongo-db-atlas-administration) <br>
- [MongoDB Atlas homepage](https://www.mongodb.com/products/platform/atlas-database) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include connector schema checks, read-only Atlas query commands, command output interpretation, and setup guidance after authentication or connection failures.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

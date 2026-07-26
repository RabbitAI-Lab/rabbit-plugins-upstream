## Description: <br>
Enables agents to read, create, and update Atlas.so customer, account, and session data through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Atlas.so operators use this skill to let an agent inspect live connector schemas, retrieve Atlas.so records, and prepare approved customer or account updates through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Atlas.so customer, account, and session data through an OOMOL-connected account. <br>
Mitigation: Connect only the intended Atlas.so account and scopes, and confirm this data access is acceptable before installing or running the skill. <br>
Risk: Write actions can create, update, or upsert Atlas.so customer and account records. <br>
Mitigation: Review the exact action name, target record, and JSON payload with the user before executing any write action. <br>
Risk: First-time setup may require installing the oo CLI. <br>
Mitigation: Use the documented installer only when the CLI is missing, and inspect the installer before running it. <br>


## Reference(s): <br>
- [Atlas.so homepage](https://atlas.so) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

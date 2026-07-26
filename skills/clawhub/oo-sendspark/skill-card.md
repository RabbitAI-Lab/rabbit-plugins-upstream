## Description: <br>
Sendspark connector skill for reading, creating, and updating Sendspark data through an OOMOL-connected account instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with Sendspark dynamic video campaigns and prospects through the oo CLI. It supports listing and retrieving campaign or prospect data, creating dynamic campaigns, and adding prospects when the user confirms the write action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create dynamic campaigns or add prospects in the connected Sendspark account. <br>
Mitigation: Confirm the exact action, target workspace or campaign, and JSON payload with the user before running any write action. <br>
Risk: Setup, authentication, connection, or billing recovery steps can affect the user's OOMOL/Sendspark account state. <br>
Mitigation: Run setup or recovery steps only after a command fails with the matching auth, connection, scope, credential, app, or billing error. <br>


## Reference(s): <br>
- [Sendspark homepage](https://sendspark.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [OOMOL Sendspark connection](https://console.oomol.com/app-connections?provider=sendspark) <br>
- [ClawHub Sendspark skill page](https://clawhub.ai/oomol/skills/oo-sendspark) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [oo connector command responses are JSON objects with data and meta.executionId when commands are run.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

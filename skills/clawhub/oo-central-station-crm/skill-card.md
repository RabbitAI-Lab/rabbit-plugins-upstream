## Description: <br>
CentralStationCRM lets an agent use an OOMOL-connected account to read, search, create, update, and delete CentralStationCRM companies, deals, people, and current-user data through the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business operators use this skill to manage CentralStationCRM records from an agent session after their OOMOL account and CentralStationCRM connection are configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read business and contact data from CentralStationCRM through an OOMOL-connected account. <br>
Mitigation: Install only when the user trusts OOMOL and the connected account has appropriate CRM access. <br>
Risk: Write actions can create or update companies, deals, and people. <br>
Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Destructive actions can delete CentralStationCRM records. <br>
Mitigation: Confirm target identifiers and obtain explicit user approval before running delete actions. <br>
Risk: Authentication, connection, or billing setup may require OOMOL account actions. <br>
Mitigation: Run setup steps only after a command fails with the matching authentication, connection, scope, expiration, or billing error. <br>


## Reference(s): <br>
- [ClawHub CentralStationCRM skill listing](https://clawhub.ai/oomol/skills/oo-central-station-crm) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [CentralStationCRM homepage](https://centralstationcrm.de) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute oo CLI connector schema and run commands when the agent follows the skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

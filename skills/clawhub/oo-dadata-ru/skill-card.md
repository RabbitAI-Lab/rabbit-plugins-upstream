## Description: <br>
DaData.ru (dadata.ru) helps agents search and read DaData.ru Suggestions API data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect DaData.ru connector schemas and run read-only Suggestions API lookups for Russian addresses, banks, emails, full names, organizations, and individual entrepreneurs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lookup inputs such as names, addresses, emails, bank names, or organization details may be sent through OOMOL to DaData.ru. <br>
Mitigation: Use the skill only for intended DaData.ru lookups and avoid submitting unnecessary personal or sensitive data. <br>
Risk: First-time setup can install or authenticate the oo CLI. <br>
Mitigation: Run setup steps only after an auth, connection, or missing-command failure and only when the user trusts the OOMOL CLI installation path. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Inspect the live action schema with oo before constructing each payload. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dadata-ru) <br>
- [DaData.ru homepage](https://dadata.ru) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector JSON responses when actions are run.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

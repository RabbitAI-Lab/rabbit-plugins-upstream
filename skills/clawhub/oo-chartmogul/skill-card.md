## Description: <br>
ChartMogul helps agents search and read ChartMogul account, customer, contact, and source data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to retrieve ChartMogul account settings, customers, contacts, and data sources with OOMOL-managed ChartMogul credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector can access customer, contact, source, and account data through the user's connected ChartMogul account. <br>
Mitigation: Use specific lookups or filtered list requests and install the skill only when that account-data access is acceptable. <br>
Risk: First-time CLI installation or authentication steps may affect the user's local environment or connected OOMOL account. <br>
Mitigation: Review any first-time oo CLI install or authentication step before running it. <br>
Risk: Future connector actions could write, overwrite, or delete ChartMogul data. <br>
Mitigation: Require explicit user confirmation before any action that writes or deletes data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chartmogul) <br>
- [ChartMogul homepage](https://chartmogul.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; connector responses are JSON objects containing data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

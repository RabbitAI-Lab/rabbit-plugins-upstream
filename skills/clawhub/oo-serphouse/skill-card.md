## Description: <br>
SERPHouse helps agents search and read SERP data through an OOMOL-connected SERPHouse account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when an agent needs to inspect SERPHouse connector schemas, look up account or credit status, list supported SERP options, or run synchronous web SERP searches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search requests and connector responses may include sensitive terms or account-related data processed by OOMOL and SERPHouse. <br>
Mitigation: Use the skill only when comfortable with OOMOL and SERPHouse processing the submitted search terms and returned data. <br>
Risk: The skill depends on the local oo CLI, user sign-in state, and an active SERPHouse connection. <br>
Mitigation: Review the OOMOL CLI install and sign-in flow before running setup commands, and retry setup only after an auth or connection error. <br>


## Reference(s): <br>
- [SERPHouse homepage](https://www.serphouse.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [SERPHouse skill page](https://clawhub.ai/oomol/skills/oo-serphouse) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON connector results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing SERPHouse action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

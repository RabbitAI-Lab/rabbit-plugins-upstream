## Description: <br>
Helps an agent use HasData through an OOMOL-connected account for public web scraping and Google SERP search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to route HasData scraping and Google SERP search requests through an OOMOL-connected account. It guides the agent to inspect live connector schemas and run read-oriented HasData actions with JSON payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, URLs, and page-scraping inputs may be sent to HasData and OOMOL-connected services. <br>
Mitigation: Avoid submitting sensitive data unless the user has approved use of the connected service for that data. <br>
Risk: First-time setup may require installing the external oo CLI. <br>
Mitigation: Review the oo CLI installer before running setup and only install it when a command fails because the CLI is missing. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Fetch the live action schema before constructing a payload. <br>


## Reference(s): <br>
- [ClawHub HasData skill page](https://clawhub.ai/oomol/skills/oo-hasdata) <br>
- [HasData homepage](https://hasdata.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON objects from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

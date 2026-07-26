## Description: <br>
Use this skill to search and read Clari Copilot data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and developers use this skill to retrieve Clari Copilot calls, transcripts, summaries, scorecards, topics, and workspace users for read-only sales conversation analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clari Copilot call transcripts, summaries, media links, and workspace user lists may contain sensitive business information. <br>
Mitigation: Install and use the skill only in workspaces where access to that Clari Copilot data is appropriate. <br>
Risk: Connector actions depend on the user's OOMOL-connected account and current Clari Copilot connection state. <br>
Mitigation: Use the documented first-time setup and connection checks only when a command fails with an authentication or connection error. <br>


## Reference(s): <br>
- [Clari Copilot Skill Page](https://clawhub.ai/oomol/skills/oo-clari-copilot) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Clari Copilot Homepage](https://www.clari.com/products/copilot/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide an agent to inspect live connector schemas and run read-only Clari Copilot connector actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

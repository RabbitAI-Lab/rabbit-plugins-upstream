## Description: <br>
Helps agents search and read HR Partner company, employee, applicant, application, job listing, and lookup data through the OOMOL HR Partner connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents assisting HR, recruiting, and people operations teams use this skill to search and read HR Partner records through an OOMOL-connected account. It supports company, employee, applicant, application, job listing, and lookup retrieval without handling raw HR Partner tokens directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive HR and recruiting records through connected HR Partner credentials. <br>
Mitigation: Use credentials scoped to users who are authorized to view the requested employee and recruiting data. <br>
Risk: The skill depends on OOMOL's oo CLI and connector service to access the HR Partner account. <br>
Mitigation: Install and use it only when the publisher, CLI, connector service, and connected account are trusted for the intended HR workflow. <br>
Risk: Connector schemas may change over time, which can make stale payloads inaccurate. <br>
Mitigation: Inspect the live connector schema before running an action and build payloads from that schema. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-hr-partner) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>
- [HR Partner homepage](https://www.hrpartner.io/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector command results are JSON when run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

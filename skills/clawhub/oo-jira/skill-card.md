## Description: <br>
Jira helps agents read Jira data and create issues or comments through an OOMOL-connected Jira account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external collaborators, developers, and support teams use this skill to search Jira projects and issues, inspect comments, create issues, and add comments from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create Jira issues or add comments. <br>
Mitigation: Confirm the exact target, payload, and expected Jira change with the user before running write actions. <br>
Risk: The skill operates through the user's OOMOL-connected Jira account. <br>
Mitigation: Install and use it only when the user wants agent access to that Jira account, and run first-time setup only after an auth or connection failure. <br>
Risk: Incorrect action payloads can produce failed or unintended Jira requests. <br>
Mitigation: Inspect the live action schema before constructing each connector payload. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-jira) <br>
- [Jira Homepage](https://www.atlassian.com/software/jira) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Jira action schemas before constructing connector payloads.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

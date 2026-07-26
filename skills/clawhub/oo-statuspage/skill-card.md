## Description: <br>
Statuspage (atlassian.com). Use this skill for ANY Statuspage request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to let an agent read and manage Atlassian Statuspage pages, components, incidents, events, and automation email settings through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Statuspage components or incidents. <br>
Mitigation: Confirm the exact page, action, and JSON payload with the user before running create or update actions. <br>
Risk: Destructive actions can delete Statuspage components or incidents. <br>
Mitigation: Require explicit user approval for the target page and component or incident before running delete actions. <br>
Risk: The connector operates through an OOMOL-connected Statuspage account. <br>
Mitigation: Install and use the skill only when the agent should manage Statuspage through OOMOL, and review account-scoped changes before approving them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-statuspage) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Statuspage](https://www.atlassian.com/software/statuspage) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use the oo CLI and return connector responses as JSON when run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

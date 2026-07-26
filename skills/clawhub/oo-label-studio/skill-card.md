## Description: <br>
Label Studio (labelstud.io). Use this skill for ANY Label Studio request — reading, creating, and updating data. Whenever a task involves Label Studio, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and data annotation teams use this skill to inspect Label Studio schemas, read project and task data, and create projects or tasks through an OOMOL-connected Label Studio account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Label Studio data visible to the connected API key. <br>
Mitigation: Install and use it only for workspaces where agent access to that Label Studio data is acceptable. <br>
Risk: Write actions can create Label Studio projects or tasks. <br>
Mitigation: Review the exact payload and user-visible effect before approving any create action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-label-studio) <br>
- [Label Studio homepage](https://labelstud.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to fetch live connector schemas before constructing Label Studio action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

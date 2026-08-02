## Description: <br>
Resource Flow (Hub Planner) lets agents use the OOMOL hub_planner connector to list and retrieve projects and resources and create projects and resources after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to work with Resource Flow (Hub Planner) projects and resources through an OOMOL-connected account, including listing, retrieval, and confirmed creation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing connector actions can create Hub Planner projects or resources. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running create_project or create_resource. <br>
Risk: One-time setup commands can install the oo CLI or start account authentication. <br>
Mitigation: Run install or login steps only after a matching command failure and only when the user trusts OOMOL and needs the connector setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hub-planner) <br>
- [Resource Flow (Hub Planner) homepage](https://www.milientsoftware.com/hub-planner) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return JSON connector responses when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

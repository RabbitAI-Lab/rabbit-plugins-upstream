## Description: <br>
Routes Pipedream requests through the OOMOL oo CLI to search and read Pipedream user, workspace, workflow, event, and app-catalog data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Pipedream account, workspace, workflow, event, and app-catalog data through an OOMOL-connected Pipedream account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive Pipedream account, workspace, workflow, and emitted-event data through connected credentials. <br>
Mitigation: Confirm the target Pipedream account, workspace, connected app, and action before allowing reads involving sensitive workflows. <br>
Risk: Authentication, connection, scope, or billing failures can block connector execution. <br>
Mitigation: Use the first-time setup and troubleshooting guidance only after a matching command failure. <br>


## Reference(s): <br>
- [Pipedream homepage](https://pipedream.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pipedream) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

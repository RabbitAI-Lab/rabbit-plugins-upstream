## Description: <br>
Permit.io (permit.io). Use this skill for Permit.io requests, including reading, creating, updating, and deleting data through the OOMOL-connected Permit.io connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Permit.io tenants, users, and role assignments from an agent through an OOMOL-connected account. It supports read operations as well as create, update, assignment, unassignment, and delete workflows that require user confirmation for state-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, assign, unassign, and delete Permit.io resources. <br>
Mitigation: Require review of the exact target, payload, and expected effect before approving write, role assignment, unassignment, or destructive actions. <br>
Risk: Using the OOMOL connector grants the agent access to the connected Permit.io environment. <br>
Mitigation: Install only for intended Permit.io administration workflows and keep the OOMOL account connection scoped and reviewed according to the user's environment controls. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Inspect the live action schema before constructing or executing payloads. <br>


## Reference(s): <br>
- [Permit.io homepage](https://www.permit.io) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-permit-io) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed oo CLI commands, action schemas, JSON payloads, and summaries of Permit.io connector results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

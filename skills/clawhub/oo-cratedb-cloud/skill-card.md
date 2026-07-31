## Description: <br>
CrateDB Cloud lets agents search and read CrateDB Cloud account and resource information through the OOMOL-connected cratedb_cloud connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect CrateDB Cloud users, organizations, projects, clusters, regions, and products through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector can expose CrateDB Cloud account and resource information visible to the connected API key. <br>
Mitigation: Install and use the skill only when the agent should read that CrateDB Cloud information through OOMOL. <br>
Risk: First-time CLI installation or login steps can change the local environment or initiate authentication flows. <br>
Mitigation: Run setup only after a matching command, authentication, or connection failure, and review installer or login steps before allowing them. <br>
Risk: Future connector actions outside the documented get and list reads could modify or delete CrateDB Cloud resources. <br>
Mitigation: Require explicit confirmation before any action tagged write or destructive, or any future action that is not one of the documented read actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cratedb-cloud) <br>
- [CrateDB Cloud homepage](https://cratedb.com/database/cloud) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-oriented connector actions; fetch the live action schema before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

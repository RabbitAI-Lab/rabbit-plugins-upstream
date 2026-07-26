## Description: <br>
Precoro (precoro.com). Use this skill for Precoro requests that read, create, or update data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to operate Precoro through the OOMOL CLI, including catalog, supplier, purchase order, user, and warehouse lookups. It also guides schema inspection and payload review before connector actions are run. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connector actions can access Precoro data through the user's OOMOL account, and future connector schemas may expose create, update, or delete operations. <br>
Mitigation: Install only when this access is intended, inspect the live connector schema before each action, and review requested payloads before running state-changing actions. <br>
Risk: The setup path includes installing and running the oo CLI. <br>
Mitigation: Use trusted OOMOL CLI installation sources and avoid repeating authentication or connection setup unless a command fails with the matching error. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-precoro) <br>
- [Precoro Homepage](https://precoro.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are expected as JSON containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

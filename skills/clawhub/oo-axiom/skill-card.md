## Description: <br>
This skill helps agents operate Axiom through the OOMOL oo CLI connector for reading, creating, querying, and deleting datasets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent manage Axiom datasets and run Axiom Processing Language queries through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector can delete Axiom datasets when a destructive action is explicitly approved. <br>
Mitigation: Require explicit confirmation of the target dataset and intended effect before running delete_dataset. <br>
Risk: Write actions can alter Axiom account state. <br>
Mitigation: Inspect the live connector schema and confirm the exact payload before running state-changing actions. <br>
Risk: The connector operates against the user's OOMOL-connected Axiom account. <br>
Mitigation: Install only when the user accepts connector access to the Axiom account, and avoid handling raw API tokens directly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-axiom) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Axiom homepage](https://axiom.co) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands should inspect the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

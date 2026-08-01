## Description: <br>
HoneyHive helps an agent read, create, update, and delete HoneyHive datasets through the OOMOL connector instead of calling the HoneyHive API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage HoneyHive datasets and datapoint associations from an agent session through OOMOL's HoneyHive connector. It supports read, write, and destructive dataset operations with schema inspection before action execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive HoneyHive actions can create, update, remove, or permanently delete dataset data. <br>
Mitigation: Confirm the exact payload, target dataset or datapoint, and expected effect with the user before running write or destructive actions. <br>
Risk: Incorrect payloads can cause failed requests or unintended HoneyHive changes. <br>
Mitigation: Fetch the live action schema with `oo connector schema` before constructing data for `oo connector run`. <br>
Risk: Authentication or connection recovery can prompt unnecessary account actions if attempted proactively. <br>
Mitigation: Use existing OOMOL-connected credentials and run setup or connection steps only after a command fails with the matching auth, scope, or connection error. <br>


## Reference(s): <br>
- [HoneyHive skill on ClawHub](https://clawhub.ai/oomol/skills/oo-honeyhive) <br>
- [HoneyHive homepage](https://www.honeyhive.ai/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions should use live schema inspection before payload construction.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

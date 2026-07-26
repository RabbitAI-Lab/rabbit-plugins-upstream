## Description: <br>
Jam lets agents search, read, and export Jam data through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect Jam connector schemas and export Jam training data for reporting or BI workflows through their connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query or export Jam data through the user's connected account. <br>
Mitigation: Install and use it only when the agent should access Jam data for the intended workflow. <br>
Risk: First-time setup may require running an oo CLI installer. <br>
Mitigation: Review the installer before running setup commands. <br>
Risk: Future connector actions may write, remove, or overwrite Jam data. <br>
Mitigation: Confirm the exact payload and effect with the user before running write actions, and require explicit approval before destructive actions. <br>


## Reference(s): <br>
- [Jam homepage](https://wejam.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wejam-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses include data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Use this skill to read, create, update, and delete Instatus data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to manage Instatus status pages, components, incidents, and incident updates through the oo CLI and an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, update, and delete actions can change Instatus status pages, incidents, components, or incident updates. <br>
Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval before destructive delete actions. <br>
Risk: Action payloads can drift from the connector contract if the live schema is not checked. <br>
Mitigation: Inspect the live oo connector schema before building each action payload. <br>


## Reference(s): <br>
- [Instatus homepage](https://instatus.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-instatus) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Persona helps agents inspect schemas and run Persona inquiry actions through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Persona inquiries from an agent, including creating inquiries from templates, retrieving and listing inquiries, and updating supported inquiry metadata after reviewing write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persona workflows can involve sensitive identity and inquiry data. <br>
Mitigation: Use a narrowly scoped Persona connection, review requested actions, and avoid exposing returned identity data beyond the user's task. <br>
Risk: Write actions can create or update Persona inquiries. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-persona) <br>
- [Persona homepage](https://withpersona.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands execute through the oo CLI and may return JSON from Persona connector actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

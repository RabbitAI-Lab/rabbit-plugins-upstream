## Description: <br>
eSignatures.com helps an agent operate eSignatures.com through an OOMOL-connected account for reading templates and contracts, creating contracts or templates, and withdrawing contracts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent manage eSignatures.com workflows through an OOMOL-connected account, including reading contract and template data and preparing account-changing actions for user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording can cause the agent to act on sensitive document workflows when an eSignatures.com request is detected. <br>
Mitigation: Use the skill only for intended eSignatures.com tasks and require the agent to show the planned action before account-changing operations. <br>
Risk: Write actions can create contracts or templates, and contract withdrawal can change signing availability. <br>
Mitigation: Require explicit user confirmation of the exact payload, target, and effect before running write or destructive actions. <br>


## Reference(s): <br>
- [eSignatures.com homepage](https://esignatures.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esignatures-io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the oo CLI to inspect live connector schemas and run eSignatures.com actions with JSON payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

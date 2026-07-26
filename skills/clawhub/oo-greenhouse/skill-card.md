## Description: <br>
Greenhouse lets agents retrieve recruiting records and add candidate notes through an OOMOL-connected Greenhouse account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiting and operations teams use this skill to query Greenhouse candidates, applications, and jobs. They can also add candidate activity notes after reviewing the exact payload and intended effect. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Greenhouse candidate and application data can contain sensitive recruiting information. <br>
Mitigation: Treat candidate and application data as sensitive and review outputs before sharing or storing them. <br>
Risk: The add_candidate_note action changes Greenhouse state. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write actions. <br>
Risk: First-time setup may require installing the oo CLI from a remote script. <br>
Mitigation: Only run the CLI install script from a trusted source and after the command fails because the CLI is missing. <br>


## Reference(s): <br>
- [ClawHub Greenhouse skill page](https://clawhub.ai/oomol/skills/oo-greenhouse) <br>
- [Greenhouse homepage](https://www.greenhouse.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Greenhouse connector calls and JSON command output when the agent runs the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

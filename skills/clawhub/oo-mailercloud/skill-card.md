## Description: <br>
Mailercloud skill for reading, creating, updating, and deleting Mailercloud data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Mailercloud via the OOMOL oo CLI, including contact, list, and contact-property workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Mailercloud contacts, contact properties, or recipient lists. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Destructive actions can delete Mailercloud contact properties. <br>
Mitigation: Confirm the target and get explicit approval before running destructive actions. <br>
Risk: Setup commands and account-connection steps affect the user's OOMOL environment. <br>
Mitigation: Run installer, login, or connection steps only when a command fails for the matching setup or authentication reason. <br>


## Reference(s): <br>
- [Mailercloud homepage](https://www.mailercloud.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

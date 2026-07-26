## Description: <br>
This skill lets agents operate Quentn (quentn.com) through an OOMOL-connected account for reading, creating, updating, and deleting CRM data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run Quentn CRM read, write, and destructive actions through the OOMOL connector while first checking each action schema and confirming state-changing payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or modify Quentn CRM records. <br>
Mitigation: Review the exact action payload and expected effect with the user before approving create, update, or set actions. <br>
Risk: Destructive actions can delete contacts or terms or remove contact-term assignments. <br>
Mitigation: Confirm the target record, action name, and payload explicitly before approving delete or remove actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-quentn) <br>
- [Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Quentn Homepage](https://quentn.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [State-changing write and destructive actions require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: skill frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

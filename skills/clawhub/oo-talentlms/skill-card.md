## Description: <br>
TalentLMS lets agents read and manage TalentLMS users and learning platform data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect TalentLMS users, courses, branches, categories, and groups, and to create, update, or delete users through an OOMOL-connected TalentLMS account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read TalentLMS account data through an OOMOL-connected account. <br>
Mitigation: Install it only for intended TalentLMS workflows and keep the OOMOL TalentLMS connection limited to the access the workflow needs. <br>
Risk: Write and destructive actions can create, update, or delete TalentLMS users. <br>
Mitigation: Review every proposed payload, confirm the exact target and intended effect, and require explicit approval before create_user, update_user, or delete_user. <br>


## Reference(s): <br>
- [ClawHub TalentLMS Skill](https://clawhub.ai/oomol/skills/oo-talentlms) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [TalentLMS](https://www.talentlms.com) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected TalentLMS API key; write and destructive actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

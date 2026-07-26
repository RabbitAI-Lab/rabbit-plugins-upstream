## Description: <br>
Manage Planka Kanban projects, boards, lists, cards, and notifications via a custom Python CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[voydz](https://clawhub.ai/user/voydz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage Planka project data from an agent-accessible CLI, including boards, lists, cards, notifications, and stored login state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an external third-party Homebrew tap for the planka-cli installer. <br>
Mitigation: Install only after deciding that you trust the voydz Homebrew tap and the planka-cli package source. <br>
Risk: Example login commands place a Planka password directly in command-line arguments. <br>
Mitigation: Prefer an interactive prompt, secure credential store, or limited-permission account instead of pasting real passwords into shell history. <br>
Risk: Card delete and bulk update commands can modify or remove Planka data. <br>
Mitigation: Confirm target IDs and intended changes before running delete, move, or bulk update operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/voydz/skills/planka) <br>
- [Publisher Profile](https://clawhub.ai/user/voydz) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the planka-cli binary and may read, create, update, move, or delete Planka records.] <br>

## Skill Version(s): <br>
0.1.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

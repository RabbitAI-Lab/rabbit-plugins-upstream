## Description: <br>
Enables an agent to operate Hashnode through an OOMOL-connected account using the oo CLI connector for reading, creating, updating, publishing, and deleting content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent manage Hashnode publications, drafts, and posts through an OOMOL-connected account while checking live action schemas before connector calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can publish, update, or delete Hashnode drafts and posts. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions. <br>
Risk: First-time setup may install or authenticate the oo CLI. <br>
Mitigation: Run setup steps only after an auth, connection, or missing-command failure, and get user approval before installation or sign-in. <br>
Risk: The skill operates the user's Hashnode account through OOMOL. <br>
Mitigation: Install and use it only when the user intends the agent to operate that account, and verify the selected publication or draft before changes. <br>


## Reference(s): <br>
- [Hashnode skill page](https://clawhub.ai/oomol/skills/oo-hashnode) <br>
- [Hashnode homepage](https://hashnode.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before each action; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

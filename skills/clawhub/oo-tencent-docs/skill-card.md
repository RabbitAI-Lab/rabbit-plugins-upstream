## Description: <br>
Tencent Docs helps agents read, create, and update Tencent Docs content through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to operate Tencent Docs from an agent workflow, including reading documents and spreadsheets, creating files, exporting files, renaming files, and updating forms or sheets after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create, rename, export, or update Tencent Docs content through the connected account. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write or destructive. <br>
Risk: The skill depends on the user's OOMOL account, oo CLI installation, and Tencent Docs connection being available. <br>
Mitigation: Run setup steps only after a matching command failure and follow the documented connection, authentication, and billing guidance. <br>


## Reference(s): <br>
- [ClawHub Tencent Docs Skill](https://clawhub.ai/oomol/skills/oo-tencent-docs) <br>
- [Tencent Docs](https://docs.qq.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

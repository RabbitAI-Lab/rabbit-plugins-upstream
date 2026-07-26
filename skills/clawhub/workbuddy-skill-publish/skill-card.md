## Description: <br>
Audit and publish agent skills to ClawHub and GitHub. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this agent skill to audit local skill directories, prepare cleaned publish copies, and publish confirmed releases to ClawHub and GitHub. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publish mode transmits selected skill files to public ClawHub and GitHub locations. <br>
Mitigation: Review the audit report, exact file list, target repositories, version, and cleaned temporary copy before confirming publication. <br>
Risk: Publish mode may modify or delete files in the remote GitHub repository. <br>
Mitigation: Use a GitHub connector token scoped only to the intended repository permissions and require explicit confirmation before remote changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/workbuddy-skill-publish) <br>
- [README](README.md) <br>
- [Chinese README](README_zh.md) <br>
- [Publish Rules for ClawHub & GitHub](references/publish-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands, file lists, checklists, and publication guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit mode is read-only; publish mode can transmit cleaned files to public services and modify remote GitHub contents after explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

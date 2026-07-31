## Description: <br>
Audit and publish agent skills to ClawHub and GitHub by scanning for personal data, validating frontmatter and bilingual documentation, removing internal-only content, and pushing clean distributions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to audit SKILL.md-based agent skills, prepare a clean publish copy, and publish to ClawHub and GitHub after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publish mode can make skill contents public on ClawHub and GitHub and may delete files in a remote GitHub repository. <br>
Mitigation: Run audit first and require explicit confirmation of the exact file list, target ClawHub and GitHub repositories, version, and remote deletions before publishing. <br>
Risk: Personal data, credentials, or internal-only notes could be exposed if included in the publish file set. <br>
Mitigation: Scan for personal data and internal-only content, publish only whitelisted files from a clean temporary copy, and block publication until findings are resolved. <br>
Risk: The workflow may read a WorkBuddy GitHub connector token during a confirmed GitHub publish operation. <br>
Mitigation: Use the token only for the confirmed repository operation, never log or persist the token value, and stop if the connector token is unavailable. <br>


## Reference(s): <br>
- [Publish Rules for ClawHub & GitHub](references/publish-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and file lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit mode is read-only; publish mode performs confirmed external publication and remote repository updates.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

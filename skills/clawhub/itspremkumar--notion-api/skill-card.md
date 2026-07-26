## Description: <br>
Read, create, update, and search Notion pages, databases, blocks, and users from a Python CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, Notion power users, and agents use this skill to automate Notion workspace reads, writes, searches, page updates, database operations, and Markdown-oriented page workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify Notion workspace content, including archiving pages. <br>
Mitigation: Use a narrowly scoped Notion integration token and test mutating commands on disposable pages before using an important workspace. <br>
Risk: The release advertises dry-run behavior, but the security evidence says that behavior does not appear to be implemented. <br>
Mitigation: Do not rely on dry-run safety unless the publisher adds and verifies an actual dry-run option. <br>
Risk: User lookup commands can print workspace member email addresses. <br>
Mitigation: Limit use of list-users and get-user to contexts where exposing member contact data is acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itspremkumar/skills/notion-api) <br>
- [Publisher Profile](https://clawhub.ai/user/itspremkumar) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; the packaged CLI emits terminal text, JSON-like structures, and Markdown depending on the subcommand.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Notion integration token such as NOTION_API_KEY for live workspace operations.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter says 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

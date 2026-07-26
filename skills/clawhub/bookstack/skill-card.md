## Description: <br>
BookStack gives an agent a CLI-backed integration for searching and managing BookStack books, chapters, pages, and shelves through the BookStack API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xenofex7](https://clawhub.ai/user/xenofex7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and documentation maintainers use this skill to automate BookStack knowledge-base workflows, including creating, editing, deleting, organizing, and searching wiki content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BookStack API credentials can grant access to wiki content and actions beyond what an agent should need. <br>
Mitigation: Use a least-privilege BookStack API token for only the intended instance and protect BOOKSTACK_TOKEN_ID and BOOKSTACK_TOKEN_SECRET like passwords. <br>
Risk: Create, update, and delete commands can alter important documentation. <br>
Mitigation: Review proposed write or delete commands carefully before running them against important BookStack content. <br>


## Reference(s): <br>
- [BookStack API documentation](https://demo.bookstackapp.com/api/docs) <br>
- [ClawHub BookStack skill listing](https://clawhub.ai/xenofex7/skills/bookstack) <br>
- [xenofex7 publisher profile](https://clawhub.ai/user/xenofex7) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and CLI output text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BOOKSTACK_URL, BOOKSTACK_TOKEN_ID, and BOOKSTACK_TOKEN_SECRET; commands can read, create, update, or delete BookStack content.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Access Readwise highlights and Reader saved articles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[refrigerator](https://clawhub.ai/user/refrigerator) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other agent users use this skill to inspect Readwise books and highlights, search saved Reader articles, export account content as JSON, and save new URLs into Reader from agent-driven workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses READWISE_TOKEN to access Readwise and Reader account data. <br>
Mitigation: Treat READWISE_TOKEN like a password, keep it out of chats and committed files, and rotate it if it may have been exposed. <br>
Risk: The Reader save command can add new URLs to the user's Reader account. <br>
Mitigation: Review save commands before execution and only run them for URLs the user intends to store. <br>


## Reference(s): <br>
- [Readwise](https://readwise.io) <br>
- [Readwise API documentation](https://readwise.io/api_deets) <br>
- [Readwise Reader API documentation](https://readwise.io/reader_api) <br>
- [Readwise access token page](https://readwise.io/access_token) <br>
- [ClawHub skill page](https://clawhub.ai/refrigerator/skills/readwise) <br>
- [Publisher profile](https://clawhub.ai/user/refrigerator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands that return JSON from the Readwise and Reader APIs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and READWISE_TOKEN; commands read account data and the Reader save command can add URLs to the user's Reader account.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

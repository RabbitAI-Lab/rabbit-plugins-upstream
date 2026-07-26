## Description: <br>
Yinxiang Skill helps agents authorize a Yinxiang/Evernote account and create, update, search, list, and organize notes, notebooks, tags, and web clips through the Yinxiang APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yinxiang-team](https://clawhub.ai/user/yinxiang-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent save, retrieve, update, move, and organize personal Yinxiang/Evernote notes after account authorization. It is intended for note workflows such as capturing Markdown content, clipping web pages, searching by filters, and managing notebooks and tags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an account token that can authorize note creation, search, retrieval, and modification. <br>
Mitigation: Install only if that level of note access is acceptable, treat the token like a password, and revoke or rotate it if it is exposed. <br>
Risk: Generic note-taking requests may save unintended content to the connected account. <br>
Mitigation: Review ambiguous capture requests before execution and confirm destructive or broad update operations, especially batch moves, tag changes, and content replacement. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yinxiang-team/skills/yinxiang-skill) <br>
- [Yinxiang API command reference](artifact/references/api-commands.md) <br>
- [Yinxiang skill authorization page](https://app.yinxiang.com/third/skills-oauth/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, api calls, markdown, configuration] <br>
**Output Format:** [Markdown guidance with bash or PowerShell commands and natural-language status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, search, read, update, move, tag, and clip notes through authenticated Yinxiang API calls.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

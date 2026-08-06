## Description: <br>
Juejin Skills helps agents query Juejin article rankings, create or publish Markdown articles through a Juejin account, and download Juejin articles as Markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content authors, and automation users can use this skill to inspect Juejin article trends, prepare Juejin drafts, publish content when explicitly authorized, and archive Juejin articles locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a Juejin account and send article content to Juejin. <br>
Mitigation: Use draft-only mode by default and require explicit review of the source file, title, tags, category, and visibility before any publish action. <br>
Risk: The skill may read local Markdown files and write downloaded articles or images under an output folder. <br>
Mitigation: Limit the agent to intended working directories and verify output locations before download or publish workflows run. <br>
Risk: Cookie-based account access can persist beyond a single workflow. <br>
Mitigation: Confirm where cookies are stored, restrict access to that storage, and know how to revoke or refresh the Juejin session. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/juejin-skills) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with possible JSON-like status summaries and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local Markdown files, write downloaded article files under an output folder, and call Juejin APIs when the agent environment permits those actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

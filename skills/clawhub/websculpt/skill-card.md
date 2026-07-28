## Description: <br>
WebSculpt bootstraps a CLI-backed browser automation workflow for external information acquisition, page scraping, API calls, and reusable browser command memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bqw1013](https://clawhub.ai/user/bqw1013) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to install or recover WebSculpt, then route work into lifecycle skills for browser automation, web data acquisition, scraping, API calls, and repeated web operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install global npm packages and persistent lifecycle skills under the user's home directory. <br>
Mitigation: Review the install scope before use and prefer project-local installation when persistent global behavior is not desired. <br>
Risk: The skill can route agents toward browser automation involving logged-in websites or private account data. <br>
Mitigation: Use it only with accounts and sessions approved for automation, and review outputs before relying on or sharing collected data. <br>
Risk: The security verdict is suspicious because the bootstrap workflow can change future agent behavior through installed lifecycle skills. <br>
Mitigation: Review and scan the installed lifecycle skills before deployment, especially in shared or production agent environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bqw1013/skills/websculpt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and routing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to install or verify WebSculpt CLI tooling and lifecycle skills before routing browser automation work.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

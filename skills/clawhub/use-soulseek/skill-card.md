## Description: <br>
Use Soulseek to search, download, and share files, chat in rooms or privately with users via its GUI or CLI tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[svidovich](https://clawhub.ai/user/svidovich) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and operators use this skill to install Soulseek or related CLI libraries, search and download files, share selected folders, and communicate with other Soulseek users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Soulseek account credentials may be exposed through shell history, environment logs, or shared operational notes. <br>
Mitigation: Use a dedicated Soulseek account and password, avoid placing credentials in shell history or logs, and prefer a neutral username. <br>
Risk: Shared-folder settings can expose private files or files the user is not authorized to distribute. <br>
Mitigation: Review shared-folder settings before use, avoid sharing private data, and only share content the user has the right to distribute. <br>


## Reference(s): <br>
- [Soulseek Downloads](https://www.slsknet.org/news/node/1) <br>
- [soulseek-cli](https://github.com/aeyoll/soulseek-cli) <br>
- [aioslsk](https://github.com/JurgenR/aioslsk) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes platform-specific installation guidance and credential handling cautions.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

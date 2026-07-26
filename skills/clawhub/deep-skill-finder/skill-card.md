## Description: <br>
Deep Skill Finder helps an agent search Meyo community skill data for task-matched skill recommendations and install a selected skill after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lintong123](https://clawhub.ai/user/lintong123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent users use Deep Skill Finder to find skill recommendations for a described task, compare the top matches, and install the selected community skill into an agent skills directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Meyo off-device. <br>
Mitigation: Avoid sensitive prompts as search queries and use the skill only when off-device search is acceptable. <br>
Risk: The skill may use local Meyo credentials and a configured or environment-supplied Meyo API host. <br>
Mitigation: Review local Meyo configuration, MEYO_API_KEY, and MEYO_API_URL before use, especially if the API host is nonstandard. <br>
Risk: The installer can download third-party skills into an agent skills directory. <br>
Mitigation: Review recommended skills before installing them, install only selected skills, and scan downloaded skill files before enabling them. <br>
Risk: Remote ZIP extraction is identified as unsafe by the security evidence. <br>
Mitigation: Install into a controlled skills directory and inspect extracted files before running the installed skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lintong123/skills/deep-skill-finder) <br>
- [Meyo skill search](https://www.meyo.life/skill) <br>
- [Meyo community](https://www.meyo.life/community/home) <br>
- [Meyo community skills](https://www.meyo.life/community/square/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown recommendations with JSON helper-script output and shell commands for search or install actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results are presented as up to five ranked skill recommendations; installation can write the selected skill into a target agent skills directory.] <br>

## Skill Version(s): <br>
1.2.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Continuous self-improvement through structured reflection and memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hopyky](https://clawhub.ai/user/hopyky) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to prompt regular self-review, record lessons learned, and reuse recent reflection notes during future work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reflection notes can persist sensitive project details, credentials, or private user data if an agent logs them. <br>
Mitigation: Configure and review the memory file as local persistent data, and instruct agents not to record secrets, credentials, private user data, or sensitive project details. <br>
Risk: The README points to an external GitHub CLI repository that was not included in the reviewed ClawHub package. <br>
Mitigation: Inspect the external CLI source before symlinking or running it, and install only from a trusted reviewed copy. <br>


## Reference(s): <br>
- [Self Reflection ClawHub listing](https://clawhub.ai/hopyky/skills/self-reflection) <br>
- [README](artifact/README.md) <br>
- [OpenClaw skill manifest](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can persist reflection entries in a local Markdown memory file and maintain timer state in a local JSON file.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

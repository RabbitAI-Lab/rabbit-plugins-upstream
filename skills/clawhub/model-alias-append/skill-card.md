## Description: <br>
Automatically appends the model alias to the end of every response with integrated hook functionality and configuration change detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ccapton](https://clawhub.ai/user/ccapton) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to add model attribution to agent responses, monitor alias configuration changes, and make it clearer which configured model generated each response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured model alias text is inserted into responses. <br>
Mitigation: Keep aliases in the OpenClaw configuration trusted and review them before deployment. <br>
Risk: The sample configuration shows a 0.0.0.0 gateway bind that may expose a local gateway if reused on an unprotected machine. <br>
Mitigation: Use a local bind unless remote access is intentional and protected by appropriate network controls. <br>


## Reference(s): <br>
- [Model Alias Append ClawHub page](https://clawhub.ai/ccapton/skills/model-alias-append) <br>
- [OpenClaw response hook documentation](https://docs.openclaw.ai/hooks#response-alias-injector) <br>
- [Model alias example image](https://github.com/Ccapton/FileRepertory/blob/master/files/model_alias_snapshot.png?raw=true) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration] <br>
**Output Format:** [Response text with an appended model alias and optional configuration-update notice] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads configured model aliases from local OpenClaw configuration and preserves response formatting.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter, package.json, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

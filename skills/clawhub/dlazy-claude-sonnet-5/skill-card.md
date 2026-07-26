## Description: <br>
This skill uses the dLazy CLI to send text, image, and video prompts to dLazy's hosted Claude Sonnet 5 service for reasoning, code generation, and complex tool orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to invoke dLazy's Claude Sonnet 5 endpoint for reasoning, coding, multimodal prompt handling, and agentic tool orchestration from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, parameters, and selected media files are sent to dLazy API and media storage endpoints for hosted inference. <br>
Mitigation: Install and use the skill only when third-party processing by dLazy is acceptable; avoid sending sensitive data unless approved for that service. <br>
Risk: A dLazy API key may be stored locally in the CLI configuration file. <br>
Mitigation: On shared systems, prefer the DLAZY_API_KEY environment variable or verify permissions on ~/.dlazy/config.json; rotate or revoke the key from the dLazy dashboard when needed. <br>
Risk: The skill depends on a third-party npm CLI package for execution. <br>
Mitigation: Use the pinned @dlazy/cli version declared by the release metadata and review the package or source before installing in controlled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON result envelope from the dLazy CLI; generated content may include text, markdown, code, or hosted output URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports a prompt plus image and video inputs; asynchronous requests may return a generateId for polling.] <br>

## Skill Version(s): <br>
1.2.7 (source: artifact frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

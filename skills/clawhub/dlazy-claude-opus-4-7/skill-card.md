## Description: <br>
Runs Claude Opus 4.7 through the dLazy CLI for multimodal prompts involving text, images, and video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to call dLazy's Claude Opus 4.7 endpoint from an agent workflow, passing text prompts and optional image or video inputs through the CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local media files are sent to dLazy's hosted service for processing. <br>
Mitigation: Avoid passing sensitive prompts or files unless the user is comfortable uploading them to dLazy. <br>
Risk: Authentication stores a dLazy API key in the local CLI configuration when using dlazy login or dlazy auth set. <br>
Mitigation: Protect the local configuration file, use per-invocation DLAZY_API_KEY when preferable, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: The skill text contains a stale npm version reference while install metadata pins @dlazy/cli@1.2.0. <br>
Mitigation: Verify the intended @dlazy/cli version before installation and prefer the pinned install command from release metadata. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-opus-4-7) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses from the dLazy CLI, with agent-facing text or generated content in result outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports asynchronous task IDs when invoked with --no-wait; media outputs and uploaded inputs may use files.dlazy.com URLs.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

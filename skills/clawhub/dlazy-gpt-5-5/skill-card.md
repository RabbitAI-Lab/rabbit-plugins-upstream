## Description: <br>
Provides access to the dLazy-hosted GPT 5.5 model for chat, writing, planning, and multimodal analysis through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to send prompts and optional image or video inputs to dLazy's hosted GPT 5.5 service through the dLazy CLI. The skill supports general chat, writing, planning, and multimodal analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, parameters, and user-supplied media paths are transmitted to dLazy's hosted API and media storage. <br>
Mitigation: Use the skill only when sending those inputs to dLazy's hosted service is acceptable, and avoid submitting sensitive data unless the user's policy permits it. <br>
Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable. <br>
Mitigation: Prefer scoped credentials, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing the key in prompts, logs, or shared shell history. <br>
Risk: Server evidence reports unavailable import provenance and notes minor package/version documentation clarity issues. <br>
Mitigation: Confirm the intended @dlazy/cli package version and review the linked package or source before relying on the release provenance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-5-5) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [JSON envelope containing generated outputs or asynchronous task status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports prompts plus optional image and video inputs; asynchronous mode can return a generateId for polling.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release metadata; artifact frontmatter reports 1.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

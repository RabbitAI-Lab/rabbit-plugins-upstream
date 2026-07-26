## Description: <br>
Generate high-quality cinematic effects videos with Google Veo 3.1. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative teams use this skill to invoke the dLazy CLI for text-to-video, image-to-video, reference-image, and video-extension generation with Google Veo 3.1. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected local media can be sent to dLazy cloud endpoints and may consume paid credits. <br>
Mitigation: Require explicit user confirmation before uploading media or running a non-dry-run generation; use dry-run mode when checking payloads and cost estimates. <br>
Risk: The API key may be persisted in ~/.dlazy/config.json, and the evidence says the referenced CLI does not clearly support the skill's file-permission claim. <br>
Mitigation: Prefer a per-invocation DLAZY_API_KEY or verify local permissions on the saved config file after login. <br>
Risk: The skill can be triggered broadly for video-generation requests. <br>
Mitigation: Confirm the user's intent, input files, generation mode, and cost-sensitive settings before starting a generation. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous generateId; dry-run can print payload and cost estimate without calling the API.] <br>

## Skill Version(s): <br>
1.3.5 (source: server evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

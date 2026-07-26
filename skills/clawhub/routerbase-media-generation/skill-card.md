## Description: <br>
Build image, video, and audio generation workflows on RouterBase, including endpoint selection, model ID verification, synchronous image responses, asynchronous video or audio polling, callback URLs, media retention handling, and migration from OpenAI-compatible image generation calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenlee123](https://clawhub.ai/user/zenlee123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to plan RouterBase media generation integrations for image, video, speech, music, and other audio workflows. It helps choose endpoints, shape requests, handle asynchronous jobs, and preserve generated media before retention expiry. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, input media URLs, and generated media requests are sent to RouterBase. <br>
Mitigation: Confirm user consent and policy fit before sending media or prompts, and avoid submitting private media URLs unless the application is authorized to share them. <br>
Risk: API keys, private media URLs, or user data could be exposed through logs or stored job metadata. <br>
Mitigation: Keep RouterBase API keys and private media URLs out of logs, and store task metadata only with appropriate access controls and retention limits. <br>
Risk: Generated media may expire before the application persists it. <br>
Mitigation: Download and store generated image, video, or audio files on the application side before RouterBase retention windows expire, and provide deletion handling where needed. <br>


## Reference(s): <br>
- [RouterBase Media Generation Notes](references/routerbase-media.md) <br>
- [RouterBase Documentation](https://docs.routerbase.com) <br>
- [RouterBase Images API](https://docs.routerbase.com/api-reference/images) <br>
- [RouterBase Overview](https://docs.routerbase.com/overview) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON, JavaScript, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes endpoint, model ID, sync or async handling, storage and retention handling, minimal request examples, and validation steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

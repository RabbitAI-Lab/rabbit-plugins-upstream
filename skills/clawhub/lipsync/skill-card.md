## Description: <br>
Lip-sync a face to a specific audio track on RunComfy via the runcomfy CLI, routing among Sync Labs, OmniHuman, Kling, Creatify, and related video models based on the user's input shape. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to select an appropriate RunComfy lip-sync route and produce the CLI invocation for making a portrait, source video, or script-driven subject speak in sync with audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media supplied for lip-sync is processed by RunComfy's cloud service. <br>
Mitigation: Use the skill only for media that may be shared with that service, and avoid private or sensitive media URLs unless external processing is acceptable. <br>
Risk: Lip-syncing a real face or voice can be misused without consent. <br>
Mitigation: Confirm rights and consent for both the target face and speaker voice before generating or distributing outputs. <br>
Risk: Third-party media URLs may be untrusted or inconsistent with the requested output. <br>
Mitigation: Use only user-provided media for the current task and review generated results for identity, voice, and synchronization mismatches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/lipsync) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>
- [Sync Labs lipsync v2](https://www.runcomfy.com/models/sync/sync/lipsync/v2?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>
- [Sync Labs lipsync v2 Pro](https://www.runcomfy.com/models/sync/sync/lipsync/v2/pro?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>
- [OmniHuman model](https://www.runcomfy.com/models/bytedance/omnihuman/api?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>
- [Kling lipsync audio-to-video](https://www.runcomfy.com/models/kling/lipsync/audio-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>
- [Kling lipsync text-to-video](https://www.runcomfy.com/models/kling/lipsync/text-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>
- [Creatify lipsync](https://www.runcomfy.com/models/creatify/lipsync?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>
- [RunComfy lip-sync catalog](https://www.runcomfy.com/models/feature/lip-sync?utm_source=clawhub&utm_medium=skill&utm_campaign=lipsync) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces runcomfy CLI invocations and route-selection guidance; generated media is handled by RunComfy.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

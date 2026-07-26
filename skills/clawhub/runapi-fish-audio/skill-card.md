## Description: <br>
Generate MP3 speech with Fish Audio through RunAPI. Use for one-off speech generation or application integration. Prefer the RunAPI CLI for one-off requests and the target-language SDK for production integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate Fish Audio MP3 speech through RunAPI, either with the RunAPI CLI for one-off requests or language SDKs for application integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text, reference audio, and transcripts are sent to RunAPI and Fish Audio for speech generation. <br>
Mitigation: Use the service only with content appropriate for RunAPI and Fish Audio, and avoid submitting sensitive text or audio unless approved for that workflow. <br>
Risk: The skill relies on local RunAPI CLI or SDK authentication, including optional API keys. <br>
Mitigation: Prefer environment-based API keys or saved RunAPI configuration, and treat the CLI, SDKs, and stored tokens as trusted local tooling. <br>


## Reference(s): <br>
- [Fish Audio model overview](https://runapi.ai/models/fish-audio.md) <br>
- [Fish Audio homepage](https://runapi.ai/models/fish-audio) <br>
- [Fish Audio provider page](https://runapi.ai/providers/fish-audio.md) <br>
- [Fish Audio s1 model](https://runapi.ai/models/fish-audio/s1.md) <br>
- [Fish Audio s2-pro model](https://runapi.ai/models/fish-audio/s2-pro.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and SDK guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference RunAPI-managed audio response fields and environment-based API key handling.] <br>

## Skill Version(s): <br>
0.1.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

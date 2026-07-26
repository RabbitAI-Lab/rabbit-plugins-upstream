## Description: <br>
Generate videos using Flyworks (a.k.a HiFly) Digital Humans, including talking photo videos from images, public avatar videos with TTS, and cloned voices for custom audio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linhui99](https://clawhub.ai/user/linhui99) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and teams use this skill to guide an agent through creating avatar-based videos, talking-photo videos, voice clones, and related Flyworks/HiFly setup steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images, audio samples, and other media provided to the skill may be uploaded to Flyworks/HiFly for processing. <br>
Mitigation: Use only portraits, voices, and media that the user owns or has explicit permission to process, and review Flyworks/HiFly retention, deletion, and acceptable-use terms before using sensitive or biometric media. <br>
Risk: The skill automatically falls back to a shared demo token when HIFLY_API_TOKEN is not configured. <br>
Mitigation: Configure a user-controlled HIFLY_API_TOKEN for normal use, and treat demo-token output as limited to watermarked videos with the documented 30-second cap. <br>
Risk: Generated avatar and cloned-voice videos can impersonate people or misrepresent consent. <br>
Mitigation: Confirm consent and intended use before creating or publishing videos, especially when using personal portraits, voice samples, or realistic public avatars. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linhui99/skills/flyworks-avatar-video) <br>
- [Authentication](references/authentication.md) <br>
- [Avatars](references/avatars.md) <br>
- [Voices](references/voices.md) <br>
- [Video Generation](references/video-generation.md) <br>
- [Flyworks](https://flyworks.ai) <br>
- [HiFly Settings](https://hifly.cc/setting) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and API result text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce generated video URLs, avatar IDs, voice IDs, and local alias records through Flyworks/HiFly API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

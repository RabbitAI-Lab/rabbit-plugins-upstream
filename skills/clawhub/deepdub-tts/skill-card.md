## Description: <br>
Generate speech audio using Deepdub and attach it as a MEDIA file (Telegram-compatible). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuval-deepdub](https://clawhub.ai/user/yuval-deepdub) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to synthesize text into speech through Deepdub and return the generated audio as a channel-ready media attachment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text submitted for synthesis is sent to Deepdub. <br>
Mitigation: Avoid sensitive text when using shared trial credentials and use your own Deepdub API key and voice prompt ID for private or production use. <br>
Risk: The Deepdub SDK dependency is unpinned. <br>
Mitigation: Pin the Deepdub SDK version in controlled or production environments. <br>


## Reference(s): <br>
- [Deepdub](https://deepdub.ai) <br>
- [ClawHub skill page](https://clawhub.ai/yuval-deepdub/skills/deepdub-tts) <br>


## Skill Output: <br>
**Output Type(s):** [Files, API Calls] <br>
**Output Format:** [MP3 audio file emitted as a MEDIA attachment path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated audio to OPENCLAW_MEDIA_DIR and returns a MEDIA path for downstream delivery.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

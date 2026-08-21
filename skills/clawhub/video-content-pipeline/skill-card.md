## Description:

Video Content Pipeline helps agents turn a written script into scene plans, AI-generated images, voiceover audio, and an assembled MP4 for faceless short-form videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content automation teams use this skill to plan scenes, generate visuals and narration, and compose short-form faceless videos for channels such as YouTube, TikTok, and Shorts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scene prompts and narration text may be sent to third-party cloud services.

Mitigation: Use the skill only with content that is appropriate to share with the disclosed image and speech services.

Risk: The optional premium scene generation path can send X402_API_KEY, a spending-capable payment credential, to a raw-IP or user-configured endpoint.

Mitigation: Verify the x402 provider and endpoint before use, keep X402_API_KEY secret, and avoid setting X402_BASE unless the destination is fully trusted.

Risk: Video composition can overwrite the selected output file.

Mitigation: Choose output paths deliberately and write generated videos to a dedicated working directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/video-content-pipeline)
- [Publisher profile](https://clawhub.ai/user/northcap-group)
- [Pollinations image endpoint](https://image.pollinations.ai)
- [Microsoft Edge TTS cloud endpoint](https://speech.platform.bing.com)
- [x402 scene generation endpoint](https://186.240.156.169:8791)
- [x402 API reference linked by the skill](https://github.com/MohamedAbdisamed/x402-api)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands; generated artifacts include JSON scene plans, PNG images, MP3 audio, and MP4 video.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3, ffmpeg, network access to disclosed third-party services, and X402_API_KEY for optional paid scene generation.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

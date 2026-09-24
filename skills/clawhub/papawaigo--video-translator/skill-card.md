## Description:

Translates or dubs user-provided video files or URLs through an online service and returns a preview_url.

This skill is ready for commercial/non-commercial use.

## Publisher:

[papawaigo](https://clawhub.ai/user/papawaigo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to submit a video file or accessible video URL for translation or dubbing, poll the remote job, and return the final preview link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided videos or URLs are sent to a disclosed third-party service.

Mitigation: Use the skill only for media the user is allowed to transmit, and avoid sending confidential or restricted videos unless the service terms and data handling are acceptable.

Risk: The video translation service API key could be exposed through prompts, logs, or command output.

Mitigation: Keep VIDEO_TRANSLATE_SERVICE_API_KEY in the environment and do not paste credential values into prompts or shared logs.

Risk: The helper script builds JSON request bodies for URL submissions and may be unsafe for untrusted URL strings.

Mitigation: Use a JSON serializer or other hardened request construction before running the helper with untrusted input.

## Reference(s):

- [API Contract (video-translator)](artifact/references/api-contract.md)
- [ClawHub Skill Page](https://clawhub.ai/papawaigo/skills/video-translator)
- [External Video Translation Service](https://audiox-api-global.luoji.cn)
- [Service Support](https://luoji.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API parameters, polling steps, and preview_url or error text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires VIDEO_TRANSLATE_SERVICE_API_KEY and sends user-provided videos or video URLs to the disclosed external service.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

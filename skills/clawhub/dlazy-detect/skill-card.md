## Description: <br>
Detect whether an image, video, or audio file is AI-generated, including visual deepfakes and the likely generator model, and return confidence scores for threshold-based decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and other external users use this skill to check image, video, or audio media for signs of AI generation, visual deepfakes, and likely generator attribution. It is intended for media analysis workflows where a structured verdict and confidence scores help inform human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local images, videos, or audio files can be uploaded to dLazy hosted services for analysis. <br>
Mitigation: Use public URLs for less sensitive material when possible, and avoid sending private, biometric, or otherwise sensitive media unless the user has accepted that data handling. <br>
Risk: The CLI can store a dLazy API key in the user's local configuration. <br>
Mitigation: Use a per-invocation DLAZY_API_KEY environment variable for short-lived access or log out after use when persistent local credentials are not appropriate. <br>


## Reference(s): <br>
- [Dlazy Detect on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-detect) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Text, Guidance] <br>
**Output Format:** [JSON detection result plus a human-readable text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires exactly one image, video, or audio input. Local files may be uploaded to dLazy media storage for hosted analysis; asynchronous runs may return a task identifier for polling.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description:

Analyzes a YouTube video link and produces a timestamped transcript of speech and key-frame visuals, together with a structured summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users who want to review a YouTube video use this skill to obtain a timestamped speech transcript, key-frame visual notes, and a structured summary for study or reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructions ask users to send a complete API key in chat.

Mitigation: Avoid installation until that request is removed, or configure the key locally without sharing it in chat.

Risk: YouTube links and related data are sent to an external parsing service.

Mitigation: Review the data transfer details and submit only links and content you are comfortable sharing with that service.

Risk: The security scan is partial because several local path references could not be resolved; it also reports promotional prompts.

Mitigation: Review the complete skill package and its prompts before installation, and reassess the security scan when all referenced files are available.

## Reference(s):

- [Skill release page](https://clawhub.ai/panting09266-ai/skills/youtube-deep-dive)
- [Cue Omni Reader online experience](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown with timestamps, speaker labels, visual notes, and structured summary sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a transcript, key-frame descriptions and on-screen text, an outline, key points, quotations, and named resources from the video.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

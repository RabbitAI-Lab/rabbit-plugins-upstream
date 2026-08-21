## Description:

Generate finished MP4 videos from narration scripts and user-provided photos using OpenRouter's asynchronous Seedance 2.0 image-to-video workflow with pre-render safety gates and ffmpeg assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn a story-telling narration script and owned photos into an assembled MP4 video. It guides model verification, privacy checks, clip generation, polling, download validation, soundtrack or subtitle handling, and ffmpeg assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Narration text and selected photos are sent to OpenRouter and related model providers.

Mitigation: Avoid confidential or sensitive images, and require explicit approval before submitting any image that contains identifiable people.

Risk: The OpenRouter API key can be used for billable video-generation requests.

Mitigation: Run short proof-of-concept clips first, use lower-cost settings for testing, and report per-clip and total cost before scaling a batch.

Risk: Frames containing recognizable people may be rejected by content or privacy policy checks.

Mitigation: Run the documented face-scan gate before submission, block flagged frames, and ask the user for alternate photos instead of retrying the same frame.

Risk: Model availability, pricing, and supported parameters can change.

Mitigation: Verify the OpenRouter video model catalog immediately before each run and stop if the requested engine or parameters are absent.

Risk: Multi-clip native audio can produce inconsistent levels or unwanted silence.

Mitigation: Default multi-clip projects to silent generated clips plus one continuous soundtrack or subtitle workflow, then check the final MP4 with playback and audio diagnostics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/video-gen)
- [OpenRouter video models endpoint](https://openrouter.ai/api/v1/videos/models)
- [OpenRouter video jobs endpoint](https://openrouter.ai/api/v1/videos)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and Python reference code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides API submission, polling, media preprocessing, ffmpeg assembly, quality checks, and final MP4 path reporting.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

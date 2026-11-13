## Description:

Clone a voice from reference audio and generate spoken audio for new text with Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide reference audio and text to generate spoken audio in a cloned voice. The skill sends prompts to dLazy's hosted API and uploads local audio inputs to its media storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a benign verdict with medium confidence, but coverage is partial and does not include the referenced CLI package or some local references.

Mitigation: Review the padded area in SKILL-cn.md and inspect the referenced CLI package before installing; treat the scan as limited evidence.

Risk: Reference audio and prompts are sent to dLazy's hosted API, and local audio files are uploaded to its media storage.

Mitigation: Use only audio you have permission to submit and avoid uploading sensitive recordings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [CLI repository link listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio URL and task status in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is hosted by dLazy; asynchronous runs may return a task ID before the audio is ready.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

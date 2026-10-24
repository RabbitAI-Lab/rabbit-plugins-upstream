## Description:

Generates speech from text with Alibaba Bailian Qwen3-TTS using system voices or natural-language custom voice designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the release to generate speech from text with system voices or custom voice descriptions. The included usage examples instead describe Recraft v4 image generation, so confirm the intended behavior before relying on it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release metadata describes Qwen3-TTS, but its usage and output examples describe Recraft v4 image generation.

Mitigation: Confirm the intended task and matching CLI command before use; do not assume this release generates speech.

Risk: Generation prompts are sent to dLazy and API use consumes service credits; the API key is stored locally.

Mitigation: Review prompts before submission, use --dry-run to preview requests, and protect or revoke the saved API key as needed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Audio files, Image files]

**Output Format:** [JSON response envelope with hosted output URLs; examples show image/png, while release metadata describes speech generation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output modality is inconsistent across the release metadata and usage examples; verify the intended task before use.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

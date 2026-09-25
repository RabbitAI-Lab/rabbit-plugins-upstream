## Description:

Generate AI videos, images and speech (text-to-video, image-to-video, reference-to-video, speech-to-video, animate, text-to-image, image-to-image, image edit, text-to-speech), bring your own LoRA models, and generate AI product/model photography for e-commerce (Image Studio) via the Phosor AI platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phosor.ai](https://clawhub.ai/user/phosor.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and e-commerce operators use this skill to submit and manage Phosor AI media generation jobs, upload input assets, manage LoRA files, synthesize speech, and generate product or model photography through Image Studio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded images, audio, video, LoRA files, and product or model photography data are sent to Phosor AI under the user's API key.

Mitigation: Use the skill only with data that may be uploaded to Phosor AI, and avoid passing private files unless that transfer is intended.

Risk: Generation, upload, LoRA, and Image Studio commands can affect service usage and billing.

Mitigation: Review billing-sensitive commands, counts, model choices, and pricing commands before execution.

Risk: The client supports a base URL override, which could send requests to an unintended endpoint.

Mitigation: Confirm that PHOSOR_BASE_URL or --base-url points to the intended Phosor endpoint before submitting jobs or uploading files.

## Reference(s):

- [Phosor AI API Reference](references/api.md)
- [Phosor AI](https://phosor.ai)
- [Phosor AI API Documentation](https://docs.phosor.ai)
- [ClawHub Skill Page](https://clawhub.ai/phosor.ai/skills/phosor-ai-skills)
- [ClawHub Publisher Profile](https://clawhub.ai/user/phosor.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands; CLI commands return JSON from Phosor AI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Phosor API key and network access to phosor.ai; generated media URLs, job status, and billing-sensitive results are returned by the remote service.]

## Skill Version(s):

1.3.1 (source: server evidence, frontmatter, README, CHANGELOG, VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

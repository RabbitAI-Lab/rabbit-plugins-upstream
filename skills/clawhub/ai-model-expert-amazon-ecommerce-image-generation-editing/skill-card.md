## Description:

Helps ecommerce, product photography, brand, and livestream commerce teams generate or edit Amazon-focused product images through AI-HIVE, including text-to-image, reference-guided image generation, task polling, and result downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, designers, and content creators use this skill to produce Amazon listing images, product-detail visuals, ad creatives, posters, social commerce images, retouching outputs, and background replacements through AI-HIVE. The skill can upload optional reference images, submit generation jobs, poll task status, and download generated image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to AI-HIVE for generation jobs.

Mitigation: Use the skill only with media and prompts you intend to upload to AI-HIVE, and avoid private, licensed, or sensitive material unless sharing is acceptable.

Risk: The skill can submit AI-HIVE generation jobs using the user's API key, including batch jobs that may incur cost.

Mitigation: Prefer explicit invocation, review routing and batch size before running, and confirm costs using the runtime pricing snapshot.

Risk: Broad implicit invocation may run the skill in contexts where external upload or job submission is not expected.

Mitigation: Review the invocation before execution and keep API keys in environment variables or the protected local config file rather than in prompts, screenshots, or public repositories.

## Reference(s):

- [AI-HIVE chat and API key entry](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-amazon-ecommerce-image-generation-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and generated image files downloaded to a local output directory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI-HIVE API key, optional reference media uploads, batch size, model parameters, routing mode, task polling, and optional no-download mode.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

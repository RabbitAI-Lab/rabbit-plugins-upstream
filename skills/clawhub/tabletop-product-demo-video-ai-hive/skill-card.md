## Description:

Helps product and content teams plan and generate tabletop top-down product demo videos by producing layouts, hand-action steps, step captions, prompts, AI-HIVE tasks, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce, marketing, social video, and product-content teams use this skill to turn authorized product assets and real operation steps into a reviewable tabletop demo video workflow. It can also help create runnable AI-HIVE commands for optional media upload, video generation, polling, download, and local video checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected media may be uploaded to AI-HIVE during generation or upload workflows.

Mitigation: Confirm that all product images, videos, audio, logos, and references are authorized before running upload or generation commands.

Risk: AI-HIVE generation tasks may incur cost.

Mitigation: Review prompts, model choice, routing mode, and price snapshot before submitting generation, and run a small sample before batch work.

Risk: The init workflow may store an API key locally in ~/.ai-hive/config.json.

Mitigation: Use environment variables or the restricted-permission config file, keep placeholder keys in examples, and avoid committing keys, logs, or screenshots containing credentials.

Risk: Generated product-demo videos can contain incorrect claims, unsafe steps, or unsupported performance promises.

Mitigation: Use real product facts and operation steps, mark uncertain claims for verification, and review outputs against platform, legal, and product-safety requirements before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/tabletop-product-demo-video-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples, JSON task records, and generated media file paths when generation is run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default workflow produces a reviewable plan before any potentially billable AI-HIVE generation task is submitted.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

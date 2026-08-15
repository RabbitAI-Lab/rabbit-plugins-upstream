## Description:

Provides multimodal image and video recognition via Doubao-Seed and Zhipu GLM, including text extraction, code generation, fallback routing, batch processing, follow-up conversations, local caching, persistent history, and optional IAM usage sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[etmnb](https://clawhub.ai/user/etmnb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to analyze selected image or video files, convert visual UI or design inputs into code, run batch recognition, and ask follow-up questions through Doubao or GLM cloud models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, videos, and prompts are sent to Volcengine or Zhipu cloud APIs.

Mitigation: Use the skill only with media and prompts approved for those providers, and avoid sensitive or regulated content unless the deployment has appropriate data-handling approval.

Risk: API keys, local media cache, history, and follow-up context are stored locally in plaintext files.

Mitigation: Avoid high-value keys on shared or synced machines, restrict filesystem access to the skill directory, and periodically remove config, cache, history, and last-response files when no longer needed.

## Reference(s):

- [Volcengine Doubao visual model documentation](https://www.volcengine.com/docs/82379/1569618)
- [Zhipu GLM platform](https://open.bigmodel.cn)
- [ClawHub skill page](https://clawhub.ai/etmnb/skills/bytedance-visual-recognition)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, and generated code snippets returned through command-line workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local config, cache, history, and last-response files; documented media limits are 15 MB for images and 50 MB for videos.]

## Skill Version(s):

5.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

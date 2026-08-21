## Description:

Generates text from prompts and optional image or video URLs using LinkFox large-language-model services, with fast and higher-quality model options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to generate writing, translations, summaries, image descriptions, and video analyses from text prompts and media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User prompts, media URLs, and the LinkFox API key are sent to a configurable remote gateway.

Mitigation: Use the skill only with a trusted LinkFox-controlled gateway and avoid submitting secrets, confidential text, private media URLs, or regulated data unless that remote processing is acceptable.

Risk: The skill can activate on broad everyday text-generation, writing, image-analysis, and video-analysis requests.

Mitigation: Review whether the request should use LinkFox's remote AIGC service before invocation, especially when the request contains sensitive or proprietary material.

Risk: Generated responses and large payloads may be retained in local LinkFox output directories.

Mitigation: Periodically clean local LinkFox output directories when retained responses may contain sensitive content.

## Reference(s):

- [AI 生文 API 参考](references/api.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-textgen)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Text or JSON response payloads; large results may be saved as JSON files with a compact JSON envelope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports content-only output for chaining, newline placeholder encoding, asynchronous polling, and local persistence of large responses.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides agents through creating ecommerce avatar selling videos with dLazy, including base portraits, scripts, TTS, avatar driving, B-roll, troubleshooting, and compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to plan and generate short-form product-selling avatar videos for TikTok Shop, Douyin, Amazon, Shopee, or brand stores with repeatable dLazy CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the dLazy CLI and dLazy services, which may receive prompts, product images, audio, and generated media.

Mitigation: Install only if you trust dLazy, use a scoped API key if available, avoid sensitive source media, and monitor account credit usage.

Risk: Generated ecommerce avatar content can create advertising, platform disclosure, or unsupported product-claim risk.

Mitigation: Review scripts, visuals, qualifications, and product claims before publishing, and label AI-generated content where platform rules require it.

Risk: Incorrect model flags, prompt lengths, encoding, or media formats can fail requests or waste paid credits.

Mitigation: Use dry runs, model-specific parameters, UTF-8 JSON input payloads, segmented audio, and explicit re-encoding when assembling videos.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [Pipeline guide](pipeline.md)
- [Base portrait recipes](recipes.md)
- [Troubleshooting and compliance notes](troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dLazy CLI command sequences, prompt recipes, configuration guidance, and troubleshooting notes; generated media is produced by external dLazy services.]

## Skill Version(s):

1.0.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

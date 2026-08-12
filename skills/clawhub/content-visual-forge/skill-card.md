## Description:

Content Visual Forge turns PDFs, webpages, articles, screenshots, transcripts, characters, and word lists into consistent visual assets such as WeChat covers, knowledge cards, learning cards, social cards, and creative micro-assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fxbin](https://clawhub.ai/user/fxbin)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, marketers, and developers use this skill to convert source material into visually consistent covers, learning cards, social card sets, prompt packages, and renderable HTML/CSS asset packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External images, logos, screenshots, or URLs may be unauthorized for production use.

Mitigation: Confirm rights and record asset sources before rendering, reuse, or commercial publication.

Risk: Production rendering can load remote resources referenced by a render package.

Mitigation: Render only trusted HTML/templates and review remote resource references before using Playwright-based output.

Risk: Generated visuals can introduce inaccurate text, data, or Chinese typography when exact copy is required.

Mitigation: Use engineering rendering for exact text and data, then run the content fidelity and quality gates before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fxbin/skills/content-visual-forge)
- [Server-resolved GitHub provenance](https://github.com/fxbin/skills/tree/main/content-visual-forge)
- [Reference navigation](references/README.md)
- [Core hard rules](references/core/hard-rules.md)
- [Execution workflow overview](references/workflows/execution-overview.md)
- [Render engine](references/render-engine.md)
- [Asset source policy](references/config/asset-source-policy.md)
- [Risk action blacklist](references/config/risk-action-blacklist.md)
- [Cover engine output schema](references/schemas/cover-engine/output.schema.json)
- [Qiaomu style atlas](https://style.qiaomu.ai/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, structured JSON data, prompt packages, and renderable HTML/CSS or image export instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include image/PDF/HTML visualization files or render packages; production rendering can use Playwright screenshots and requires authorized asset source records.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; artifact internal VERSION is v2.7.3, while manifest and skill docs report 2.7.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

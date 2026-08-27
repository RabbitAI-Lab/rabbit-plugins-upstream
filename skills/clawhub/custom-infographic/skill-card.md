## Description:

Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Original author 宝玉 (JimLiu); ported & customized by j3ffyang. Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn articles, documents, URLs, or topics into infographic workflows, prompts, and generated images with selectable layouts, styles, aspect ratios, and languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The final assembled infographic prompt may be sent to OpenRouter.

Mitigation: Avoid sensitive documents unless secrets are removed, and use OPENROUTER_API_KEY only in environments where image generation is intended.

Risk: Image models may render labels inaccurately or omit required text.

Mitigation: Use the skill's text accuracy block and verify generated image text against the expected text list before delivery.

## Reference(s):

- [Upstream baoyu-infographic](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)
- [Analysis framework](references/analysis-framework.md)
- [Structured content template](references/structured-content-template.md)
- [Base prompt](references/base-prompt.md)
- [Workflow example](references/workflow-example.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, image]

**Output Format:** [Markdown files, prompt text, shell commands, and PNG image output when generation succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates working files under infographic/{topic-slug}/ and a final image under imgs/; requires OPENROUTER_API_KEY for image generation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

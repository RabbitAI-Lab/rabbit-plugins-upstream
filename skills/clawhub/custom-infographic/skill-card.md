## Description:

Generates professional infographics from articles, documents, URLs, or topics using a 21-layout by 21-style system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and teams use this skill to turn source material into structured infographic content, an image-generation prompt, and optionally a rendered image through a configured image service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes source-derived working files locally.

Mitigation: Use it only with content appropriate for local workspace storage and review generated working files before sharing them.

Risk: The final prompt can be sent to OpenRouter or another image service.

Mitigation: Review generated prompts for secrets, personal data, proprietary text, and licensing-sensitive material before image generation or external copy/paste.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/custom-infographic)
- [Upstream baoyu-infographic](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)
- [Analysis framework](references/analysis-framework.md)
- [Structured content template](references/structured-content-template.md)
- [Base prompt](references/base-prompt.md)
- [Workflow example](references/workflow-example.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown working files, an image-generation prompt, and optional PNG output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires a configured OPENROUTER_API_KEY; without it, the skill produces prompt-only artifacts for external use.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

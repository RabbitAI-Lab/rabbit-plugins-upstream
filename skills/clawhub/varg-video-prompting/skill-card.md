## Description:

Guides agents in choosing varg video, image, voice, and music models, writing effective prompts, and checking generated media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams can use this skill to select a varg model, prepare reusable image and video prompts, plan audio, and review generated clips for defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Footage or voice recordings may be sent to external services without a clear privacy check.

Mitigation: Before uploading media, confirm that you have permission to share it and review the external service's privacy terms.

Risk: The security guidance flags an unpinned installer, which can change between runs.

Mitigation: Review the installer source and pin a known version or commit before relying on it.

Risk: Retry advice for moderation-rejected requests could be read as encouraging filter evasion.

Mitigation: Do not retry unchanged prompts to bypass moderation; revise the request to comply with the model provider's policy or stop.

## Reference(s):

- [Prompt templates](artifact/references/prompt-templates.md)
- [Model guide](artifact/references/models.md)
- [MCP tools guide](artifact/references/mcp-tools.md)
- [Look references guide](artifact/references/look-references.md)
- [Examples](artifact/references/examples.md)
- [varg model catalog](https://varg.ai/models/llms.txt)
- [Seedance 2.5 model notes](https://varg.ai/models/seedance_2_5.md)
- [varg.ai](https://varg.ai)
- [ClawHub skill page](https://clawhub.ai/vargai/skills/varg-video-prompting)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown guidance with reusable prompts, model recommendations, and QA checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and recommendations are intended for use with varg media-generation models.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

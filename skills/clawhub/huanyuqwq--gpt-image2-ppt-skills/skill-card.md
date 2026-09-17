## Description:

Generate visually striking presentation slide PNGs and 16:9 PPTX decks with OpenAI gpt-image-2, using built-in styles or a user-supplied PPTX template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanyuqwq](https://clawhub.ai/user/huanyuqwq)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and skill-compatible agents use this skill to turn a presentation topic, outline, slide plan, or template into polished decks. It is best suited for reports, pitches, training materials, product introductions, and similar presentation workflows where visual quality and quick iteration matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide text, templates, and reference images may be sent to configured model endpoints.

Mitigation: Use trusted provider URLs, avoid sensitive material unless approved for that endpoint, and review what content will be included before generation.

Risk: Install, update, dependency, and image-download paths introduce credential and network-boundary risk.

Mitigation: Use a dedicated virtual environment or pinned dependencies, review downloads and generated files before use, and run the skill only in environments where outbound model traffic is acceptable.

Risk: The optional codex backend can launch a child full-auto agent.

Mitigation: Avoid that backend unless the operator explicitly accepts the delegated agent behavior and reviews the resulting files.

Risk: API keys stored in a skill .env may be temporarily backed up under /tmp during updates.

Mitigation: Prefer agent, system, CI, or secret-manager injection for API keys and avoid storing long-lived secrets in the skill .env.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huanyuqwq/skills/gpt-image2-ppt-skills)
- [ClawHub publisher profile](https://clawhub.ai/user/huanyuqwq)
- [OpenAI Images guide](https://platform.openai.com/docs/guides/images)
- [README](artifact/README.md)
- [English README](artifact/docs/README.en.md)
- [Editing capability guide](artifact/docs/edit_guide.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance, JSON slide plans, shell commands, generated images, and PPTX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates per-slide PNGs, a 16:9 PPTX, run metadata, and optional editable PPTX review assets when explicitly requested.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

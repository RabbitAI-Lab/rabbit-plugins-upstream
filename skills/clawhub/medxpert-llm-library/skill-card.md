## Description:

Guides users through running local language models and building a personal knowledge library on modest hardware.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (.py code only); all rights reserved (skill text and methodology)

## Use Case:

Individuals and teams use the skill to set up Ollama, organize local documents, generate summaries, and answer questions from a personal knowledge library.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Summarizing or asking questions can send local document content to a configured model endpoint, which may not be local.

Mitigation: Verify OLLAMA_BASE points to localhost or 127.0.0.1 before using sensitive documents; use only a trusted, controlled endpoint.

Risk: Setup creates local library files and may initialize Git metadata.

Mitigation: Review the target library location and setup effects before running the helper.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-llm-library)
- [MedXpert website](https://medxpert.cn)
- [Ollama download](https://ollama.com/download)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown instructions and text-based summaries or answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can write a local Markdown library index.]

## Skill Version(s):

1.29.4 (source: ClawHub release metadata; bundled files identify 1.29.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

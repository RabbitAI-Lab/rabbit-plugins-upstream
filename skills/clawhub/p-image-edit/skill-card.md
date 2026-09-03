## Description:

Use when someone wants to edit an existing photo, change outfits or backgrounds, compose from reference images, or apply prompt-driven edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operators use this skill to guide image-editing workflows for existing photos, including background changes, outfit edits, and multi-reference compositions through Pruna's p-image-edit API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and edit prompts are sent to Pruna's external API.

Mitigation: Use only images and prompts intended for Pruna processing, and avoid submitting sensitive photos unless sharing them with that service is intended.

Risk: The workflow requires a Pruna API key.

Mitigation: Keep PRUNA_API_KEY in an environment variable or secret store and avoid exposing it in prompts, logs, files, or shared transcripts.

Risk: The skill may suggest installing prerequisite skills before running the workflow.

Mitigation: Review suggested prerequisite skill installs before accepting them.

Risk: Prompt-driven edits can unintentionally alter image details the user wanted preserved.

Mitigation: Use explicit keep-clauses for identity, pose, lighting, background, or product details, and review the proposed prompt before submitting the API request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-edit)
- [Pruna file upload endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and one to five uploaded image URLs; may send prompts and selected images to Pruna's external API.]

## Skill Version(s):

1.0.10 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

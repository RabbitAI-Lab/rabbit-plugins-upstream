## Description:

Helps an agent edit existing photos by changing outfits or backgrounds, composing from reference images, and drafting prompt-driven edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to prepare faithful image-edit prompts, upload source or reference images to Pruna, and run the p-image-edit API flow while preserving user-specified details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Photos and prompts are sent to Pruna's API.

Mitigation: Use the skill only when sharing those inputs with Pruna is acceptable for the user's data handling requirements.

Risk: The skill asks agents to install multiple mutable external skills with unpinned npx commands.

Mitigation: Review and pin dependent skill versions before allowing an agent to run the installation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-edit)
- [Pruna file upload API](https://api.pruna.ai/v1/files)
- [Pruna predictions API](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl command examples and API parameter notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires source images or reference image URLs and a PRUNA_API_KEY before API calls.]

## Skill Version(s):

1.0.13 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

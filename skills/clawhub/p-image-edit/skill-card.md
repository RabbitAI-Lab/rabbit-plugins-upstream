## Description:

Use when someone wants to edit an existing photo -- change outfits or backgrounds, compose from reference images, or apply prompt-driven edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through prompt-locked edits of existing images, including background changes, outfit changes, and multi-reference compositions through Pruna's image editing API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install multiple unpinned remote skills with automatic approval.

Mitigation: Review referenced Pruna skills before installation and prefer pinned versions or remove automatic approval so changes can be reviewed.

Risk: The workflow sends source images and prompts to an external API.

Mitigation: Avoid submitting sensitive or non-consented images and prompts unless Pruna's data handling terms are acceptable for the use case.

## Reference(s):

- [p-image-edit ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-edit)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with curl commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides prompt construction, reference image upload, async prediction creation, polling, and follow-on image or video workflow choices.]

## Skill Version(s):

1.0.12 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description: <br>
Use when someone wants to edit an existing photo - change outfits or backgrounds, compose from reference images, or apply prompt-driven edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide prompt-driven edits of existing images with Pruna's p-image-edit model, including background changes, outfit changes, multi-reference composition, and faithful surgical edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uploads user-provided images and prompts to Pruna's cloud API. <br>
Mitigation: Use only images intended for upload and install the skill only if cloud processing by Pruna is acceptable. <br>
Risk: The skill requires PRUNA_API_KEY for API calls. <br>
Mitigation: Keep the API key in environment configuration and do not paste or store it in prompts, command history, or generated artifacts. <br>
Risk: The workflow references optional safety-related fields such as disable_safety_checker. <br>
Mitigation: Avoid changing safety-related options unless the user understands the policy and account implications. <br>
Risk: The workflow includes npx commands to install related skills. <br>
Mitigation: Review related skill installs before running the commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-edit) <br>
- [Pruna files API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with curl command examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY; uploads 1-5 user-provided image references; supports optional aspect_ratio, turbo, seed, and disable_safety_checker fields.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

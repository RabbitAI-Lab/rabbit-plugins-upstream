## Description: <br>
Use when someone wants to edit an existing photo -- change outfits or backgrounds, compose from reference images, or apply prompt-driven edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide an agent through controlled edits of existing photos, including reference-image handling, prompt drafting, fidelity checks, and Pruna API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uploads user-provided source images, prompts, and edit parameters to Pruna's API. <br>
Mitigation: Use it only with images and prompts appropriate for Pruna processing, and review Pruna's data handling terms before using sensitive personal images. <br>
Risk: The skill requires PRUNA_API_KEY for API calls. <br>
Mitigation: Keep the key in the environment, avoid exposing it in shared logs or transcripts, and rotate it if disclosure is suspected. <br>


## Reference(s): <br>
- [ClawHub p-image-edit listing](https://clawhub.ai/pruna-ai/skills/p-image-edit) <br>
- [Pruna file upload endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with curl command blocks and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-provided source images; prompts, image URLs, and edit parameters are sent to Pruna's API.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

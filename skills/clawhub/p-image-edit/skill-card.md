## Description: <br>
Use when someone wants to edit an existing photo — change outfits or backgrounds, compose from reference images, or apply prompt-driven edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to guide photo edits with Pruna's p-image-edit model, including reference upload, prompt drafting, aspect-ratio selection, and async prediction calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected reference images and prompts are sent to Pruna's API for editing. <br>
Mitigation: Use the skill only when external API processing is acceptable, and avoid submitting images or prompts that should not leave the runtime environment. <br>
Risk: The skill depends on a PRUNA_API_KEY from the environment. <br>
Mitigation: Store the key in runtime secrets or environment variables and do not paste the raw key into chat or generated files. <br>
Risk: The skill suggests installing related Pruna skills with npx, including an optional full-suite install. <br>
Mitigation: Review the related skill packages and requested install command before allowing installation. <br>
Risk: The skill exposes disable_safety_checker as an optional request field. <br>
Mitigation: Require explicit user intent and content-policy review before using safety-checker bypass options. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-edit) <br>
- [Pruna file upload API](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides prompt construction, reference-image upload, and Pruna prediction requests; required inputs are a prompt and one to five image URLs.] <br>

## Skill Version(s): <br>
1.0.7 (source: evidence.release.version and SKILL.md metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

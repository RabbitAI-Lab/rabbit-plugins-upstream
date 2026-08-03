## Description: <br>
Use when someone wants a fast AI image, such as product shots, hero visuals, mood boards, or draft photos from a text prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to guide agents through Pruna text-to-image generation, including prompt intake, aspect-ratio selection, API request construction, and follow-on image workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Pruna's external API and requires a PRUNA_API_KEY credential. <br>
Mitigation: Keep the API key out of prompts, logs, and committed files, and review generated curl commands before execution. <br>
Risk: The optional disable_safety_checker field can reduce model safety controls. <br>
Mitigation: Use disable_safety_checker only for clearly authorized, policy-compliant work; otherwise leave safety checking enabled. <br>


## Reference(s): <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with curl commands and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and can pass prompt, aspect_ratio, seed, LoRA, Hugging Face token, and safety-checker options to the Pruna API.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

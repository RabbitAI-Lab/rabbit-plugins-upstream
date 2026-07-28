## Description: <br>
Image Edit - Pro Pack on RunComfy helps an agent transform existing images by routing background swaps, object edits, text rewrites, multi-reference edits, and mask-based edits to the appropriate RunComfy model endpoint through the local RunComfy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and production teams use this skill to edit existing images from natural-language instructions, including background changes, object removal or addition, in-image text replacement, batch edits, multi-reference composition, and mask-constrained region replacement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image URLs, masks, and edit prompts are sent to RunComfy for processing. <br>
Mitigation: Use only content approved for RunComfy processing, and avoid private or sensitive images unless that exposure is acceptable. <br>
Risk: The skill depends on RunComfy CLI authentication and local token configuration. <br>
Mitigation: Use an approved RunComfy account or RUNCOMFY_TOKEN and protect the local RunComfy configuration directory. <br>
Risk: External source image and mask URLs are fetched by the RunComfy service. <br>
Mitigation: Treat external URLs as untrusted inputs and review generated results before using them in production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/image-edit-runcomfy) <br>
- [RunComfy homepage](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=image-edit-runcomfy) <br>
- [RunComfy image edit models](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=image-edit-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown with bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The RunComfy CLI may download edited image files into the requested output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

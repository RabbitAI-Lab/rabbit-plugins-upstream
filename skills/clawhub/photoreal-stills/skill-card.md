## Description: <br>
Generate still images that read as real photographs rather than AI renders across candid portrait, editorial, documentary, food, architectural, lifestyle, stock-style, reportage, and interior use cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to guide an agent through selecting live Runware image models, constructing photoreal prompts, generating small batches of still images, and judging outputs against a realism checklist. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt content or reference images may be sent to external image-generation services. <br>
Mitigation: Review user-provided content for sensitivity and confirm that external provider use is acceptable before invoking image-generation tools. <br>
Risk: Image-generation calls may incur provider costs, especially when requesting batches or higher-fidelity models. <br>
Mitigation: Confirm model choice, batch size, and cost expectations before running generation. <br>
Risk: Photorealistic outputs can be mistaken for camera-captured images. <br>
Mitigation: Apply appropriate disclosure, provenance, or review practices for contexts where viewers could be misled. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/runware/skills/photoreal-stills) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text] <br>
**Output Format:** [Markdown guidance with prompt structure, model-selection notes, parameter guidance, and quality checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead the agent to make external image-generation tool calls and select generated still-image variants when used with the related Runware skills.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

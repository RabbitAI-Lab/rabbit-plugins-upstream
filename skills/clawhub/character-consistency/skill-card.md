## Description: <br>
Keeps the same character, person, or product consistent across generated scenes, poses, outfits, and styles by using reference images and identity-anchored prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and creative operators use this skill to generate new images of an established character, person, mascot, or product while preserving identity across new scenes, poses, outfits, and styles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reference images may include private faces, confidential product images, or copyrighted material that would be sent to the image-generation provider. <br>
Mitigation: Use only reference images the user has permission to process and is comfortable sending to the provider. <br>
Risk: Generated outputs can drift from the intended subject identity or unintentionally change details outside the requested variation. <br>
Mitigation: Review outputs against the supplied references and retry drifted results with clearer or additional references. <br>


## Reference(s): <br>
- [Worked recipes](references/examples.md) <br>
- [Character Consistency on ClawHub](https://clawhub.ai/runware/skills/character-consistency) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown guidance with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include image-generation prompts, reference-image inputs, dimensions, seeds, and result review criteria.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

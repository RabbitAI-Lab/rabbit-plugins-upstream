## Description: <br>
Mad Story helps agents design cinematic storyboards and media-generation prompts for video and image workflows, including Seedance video prompts, Seedream image prompts, and short-drama planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, directors, and production teams use this skill to turn concepts, product briefs, reference images, or short-drama ideas into storyboard plans and structured prompts for supported video and image generation platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advanced modes may be incomplete if referenced helper files are not available with the installed skill. <br>
Mitigation: Confirm the referenced files are packaged before relying on advanced modes, or use the core SKILL.md workflows only. <br>
Risk: Generated prompts are calibrated for Seedance 2.0 video and Seedream 4.x/5.x image workflows, while other platforms may require manual parameter adaptation. <br>
Mitigation: Verify the target platform and adjust platform-specific parameters before production use. <br>
Risk: Generated media can still show long-duration quality loss, motion instability, or cross-shot character inconsistency. <br>
Mitigation: Review generated outputs manually, keep complex shots shorter where possible, and regenerate or revise prompts when consistency checks fail. <br>


## Reference(s): <br>
- [Server-resolved GitHub source repository](https://github.com/qomob/madstory) <br>
- [ClawHub skill page](https://clawhub.ai/qomob/skills/madstory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown storyboard plans with structured prompt blocks and platform parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sections such as STANDARD_PROMPT, NEGATIVE_PROMPT, TIMELINE, CAMERA, MOTION_STRENGTH, IMAGE_PROMPT, TEXT_CONTENT, and platform-specific settings.] <br>

## Skill Version(s): <br>
3.4.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

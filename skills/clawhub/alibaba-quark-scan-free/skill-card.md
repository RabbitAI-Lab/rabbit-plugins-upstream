## Description: <br>
Alibaba Quark Scan Free helps agents process user-provided images with Quark Scan scenarios for image enhancement, handwriting removal, and document scan optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to route image enhancement, handwriting removal, and document scanning requests to the Quark Scan service. It is intended for workflows where users can provide image URLs, local image paths, or Base64 image data and review returned JSON results and generated image paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to execute an unspecified local Python script or wrapper. <br>
Mitigation: Inspect and approve the actual script path and command before allowing execution. <br>
Risk: Images are sent to the Quark Scan service for processing. <br>
Mitigation: Use the skill only with images that are appropriate to send to that service. <br>
Risk: Generated images may remain in a temporary directory until manually deleted. <br>
Mitigation: Review returned local paths and remove temporary output files when they are no longer needed. <br>
Risk: The artifact contains conflicting claims about batch processing support. <br>
Mitigation: Treat single-image processing as the supported baseline unless the installed wrapper proves batch behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/alibaba-quark-scan-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [Quark Scan business portal](https://scan.quark.cn/business) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON service results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return execution status, result data, execution logs, errors, and local temporary image paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

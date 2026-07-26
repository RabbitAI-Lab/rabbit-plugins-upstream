## Description: <br>
Byted Mediakit Image helps agents use MediaKit CLI image tools for OCR, background removal, image erasure and repair, image enhancement, and image-quality evaluation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volcvnebot](https://clawhub.ai/user/volcvnebot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run cloud image-processing workflows through MediaKit CLI, including OCR, background removal, object or text erasure, enhancement, and quality scoring. It is intended for image-domain tasks where the user can provide appropriate image inputs and MediaKit credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted images are processed by a cloud MediaKit service and may include private, regulated, confidential, or sensitive content. <br>
Mitigation: Use the skill only with images the user is authorized to submit, and review the provider's handling and retention terms before processing sensitive material. <br>
Risk: The skill requires installing and trusting the MediaKit CLI provider and configuring a MediaKit API key. <br>
Mitigation: Install MediaKit CLI only from a trusted source, protect API credentials, and verify the active MediaKit configuration before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/volcvnebot/skills/byted-mediakit-image) <br>
- [MediaKit shared rules](reference/shared.md) <br>
- [Image OCR](reference/image-ocr.md) <br>
- [Erase image](reference/erase-image.md) <br>
- [Remove image background](reference/remove-image-background.md) <br>
- [Enhance image](reference/enhance-image.md) <br>
- [Evaluate image quality](reference/evaluate-image-quality.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud-only synchronous MediaKit image operations return final results directly.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

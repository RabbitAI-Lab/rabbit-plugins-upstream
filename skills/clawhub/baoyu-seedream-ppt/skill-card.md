## Description: <br>
Generates image-based presentation decks from user content using the Baoyu infographic layout framework and the Doubao Seedream 5.0 text-to-image model, with selectable layouts, styles, and aspect ratios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cindypapa](https://clawhub.ai/user/cindypapa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to turn structured source material into a slide deck made of generated infographic images. It supports a guided workflow that analyzes content, recommends layout and style combinations, generates prompts, calls Seedream for images, and packages the results into a PPTX file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected slide content and generated prompts are sent to Volcengine/Seedream using the configured API key. <br>
Mitigation: Use the skill only with content that is approved for that external service, and avoid confidential documents unless processing permission is clear. <br>
Risk: Generated prompts may contain sensitive presentation details before image generation. <br>
Mitigation: Review generated prompts before the final image-generation step, especially for sensitive presentations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cindypapa/skills/baoyu-seedream-ppt) <br>
- [Project homepage](https://github.com/JimLiu/baoyu-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated prompt/configuration files; final assets are PNG images and a PPTX deck.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the selected layout, visual style, aspect ratio, and content file to generate one image per slide before assembling the presentation.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

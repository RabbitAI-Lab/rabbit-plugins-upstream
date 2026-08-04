## Description: <br>
极简海报 generates poetic minimalist zine-poster prompts and matching raster images from a theme, sentence, object, mood, brief, or photo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chugenice](https://clawhub.ai/user/chugenice) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill to turn compact creative inputs into a quiet Japanese/Korean zine-style poster concept, final image-generation prompt, generated bitmap image, and short recipe summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ambiguous poster requests may route into this opinionated minimalist zine style and invoke ImageGen credits. <br>
Mitigation: Tell the user before image generation that ImageGen may consume credits, and honor prompt-only requests when explicitly given. <br>
Risk: Reference photos provided for incorporation are passed to the image-generation tool. <br>
Mitigation: Use only reference images that are appropriate to send to the image-generation service, and avoid sensitive or private photos. <br>
Risk: Generated images may miss the strict visual requirements, such as sparse paper composition or a visible high-chroma anchor. <br>
Mitigation: Inspect the result against the skill quality gate and regenerate once with tighter prompt wording when the selected mode or recipe is not met. <br>


## Reference(s): <br>
- [Visual Rules - Minimal Zine Poster](artifact/references/visual-rules.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/chugenice/skills/minimalist-poster-prompt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Images] <br>
**Output Format:** [Markdown with a generated image, final image prompt, and recipe summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke ImageGen and may use a user-provided reference photo for image-to-image generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

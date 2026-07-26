## Description: <br>
Generate professional infographics with 21 layout types and 22 visual styles, including content analysis, layout and style recommendations, and publication-ready infographic generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cindypapa](https://clawhub.ai/user/cindypapa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert source content into structured infographic plans, choose appropriate layout and visual style combinations, and generate raster infographic assets through an available image-generation backend. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source content and reference images may be written into local output files and sent to the selected image-generation backend. <br>
Mitigation: Avoid using confidential material unless the chosen backend and local storage location are approved for that content. <br>
Risk: Generated infographic text or visual structure may be incorrect, incomplete, or misleading. <br>
Mitigation: Review generated prompts and final infographic assets before publication or distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cindypapa/skills/baoyu-infographic) <br>
- [Project homepage](https://github.com/JimLiu/baoyu-skills#baoyu-infographic) <br>
- [Analysis framework](references/analysis-framework.md) <br>
- [Structured content template](references/structured-content-template.md) <br>
- [Codex image generation backend](references/codex-imagegen.md) <br>
- [Preferences schema](references/config/preferences-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and generated project files, including analysis, structured content, image prompts, and raster infographic output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a topic-scoped output directory and requires confirmation before image generation unless the user explicitly skips confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

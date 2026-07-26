## Description: <br>
image-deck helps an agent create image-only slide decks, single slides, PowerPoint-style presentations, and carousel pages using GPT Image 2, with planning, prompt review, sample approval, slide generation, and QA steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tseng71](https://clawhub.ai/user/tseng71) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and presentation authors use this skill when they want an agent to plan and generate complete raster-image slides, then optionally assemble them into PPTX or PDF deliverables. It is best suited to decks where each page is a finished generated image rather than an editable PowerPoint layout. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may read source material, perform research, save local prompt or log files, and use image generation. <br>
Mitigation: Review source sensitivity before use and inspect generated prompts, logs, and image outputs before sharing or publishing. <br>
Risk: Some required confirmation wording is Chinese-only despite support for non-Chinese decks. <br>
Mitigation: Non-Chinese users should check approval prompts carefully and provide explicit approval only after reviewing the design and sample style. <br>
Risk: Generated raster slides may contain unreadable or incorrect visible text and are not ordinary editable PowerPoint pages. <br>
Mitigation: Inspect each generated slide at full size and regenerate failed slides; use an editable-presentation workflow when precise editable text, charts, or tables are required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tseng71/skills/image-deck) <br>
- [Publisher profile](https://clawhub.ai/user/tseng71) <br>
- [Prompt Patterns](artifact/references/prompt-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with prompt templates, approval language, file paths, and optional PPTX/PDF assembly instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce research notes, visual bibles, per-slide prompts, image-generation logs, generated slide images, and deck packaging instructions.] <br>

## Skill Version(s): <br>
0.1.20 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

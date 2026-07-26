## Description: <br>
AI-driven multi-format SVG content generation system that converts source documents into high-quality SVG pages and exports them to PPTX through multi-role collaboration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yz6214589-hash](https://clawhub.ai/user/yz6214589-hash) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content creators, and presentation authors use this skill to turn PDFs, DOCX files, PPTX files, spreadsheets, web pages, URLs, or Markdown into structured slide decks with SVG pages, optional generated imagery, narration, live preview, quality checks, and editable PPTX export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes local documents and may move imported source files into its project folder. <br>
Mitigation: Use the copy mode when preserving original files matters, and review which local files are imported into each project. <br>
Risk: Image generation, TTS, web conversion, and image search can use configured API keys or fetch external web resources. <br>
Mitigation: Keep .env files private, configure only the providers needed for the task, and avoid importing sensitive private URLs on untrusted networks. <br>
Risk: Generated SVG slides, PPTX exports, images, and narration may need human review before presentation or distribution. <br>
Mitigation: Use the included quality checks and preview workflow, then review exported decks for factual accuracy, visual fidelity, licensing, and audience suitability. <br>


## Reference(s): <br>
- [Dog Slide ClawHub Page](https://clawhub.ai/yz6214589-hash/skills/dog-slide) <br>
- [README](artifact/README.md) <br>
- [Script Documentation](artifact/scripts/README.md) <br>
- [SVG Pipeline Documentation](artifact/scripts/docs/svg-pipeline.md) <br>
- [Conversion Tools Documentation](artifact/scripts/docs/conversion.md) <br>
- [Chart Templates](artifact/templates_charts/README.md) <br>
- [Layout Templates](artifact/templates_layouts/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, SVG/code artifacts, and generated presentation files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary generated artifacts are SVG pages and editable PPTX exports; optional outputs include images, narration audio, animation configuration, and preview/editor state.] <br>

## Skill Version(s): <br>
2.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

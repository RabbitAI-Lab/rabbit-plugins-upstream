## Description: <br>
Extract data from chart or graph images and produce a structured table with confidence levels and CSV-ready reconstructed source data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to digitize chart images into structured tables, confidence annotations, observations, and CSV-ready output for spreadsheet or chart reconstruction workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Extracted chart values can be wrong when the source image is low resolution, axes are ambiguous, scales are logarithmic, or data points overlap. <br>
Mitigation: Review extracted values manually when precision matters and verify low-confidence or interpolated points against the original chart. <br>
Risk: The skill may report misleading precision if the chart only supports coarse visual reading. <br>
Mitigation: Require assumptions, caveats, grid resolution, and confidence levels to be included with the extracted data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/chart-data-extractor) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/chart-data-extractor.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, csv, guidance] <br>
**Output Format:** [Markdown sections with structured tables, confidence notes, observations, caveats, and CSV code blocks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Flags low-confidence values separately and states assumptions about axes, scale, interpolation, and image quality.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

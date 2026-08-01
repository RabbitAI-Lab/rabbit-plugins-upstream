## Description: <br>
hv-analysis guides an agent through web-backed horizontal-vertical analysis of a product, company, concept, technology, or person and produces a structured research report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qpoison](https://clawhub.ai/user/qpoison) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, analysts, and operators use this skill to collect current evidence, compare a subject across history and competitors, and turn the findings into a long-form research report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate broad web-backed research and may spawn subagents, which can collect noisy or unreliable information. <br>
Mitigation: Require source citations for key claims and review the final report before using it for decisions. <br>
Risk: The workflow may install Python packages and run a Markdown-to-PDF conversion script. <br>
Mitigation: Confirm package installation commands before execution and run the workflow in an isolated environment when possible. <br>
Risk: The skill writes Markdown, HTML, and PDF report files into the workspace. <br>
Mitigation: Confirm output paths before execution and inspect generated files before sharing or relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qpoison/skills/hv-analysis) <br>
- [Horizontal-Vertical Analysis schema](references/schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown research report with optional HTML and PDF files generated from the bundled conversion script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces long-form Chinese research reports with source lists, horizontal and vertical analysis sections, cross-axis insights, and optional PDF formatting.] <br>

## Skill Version(s): <br>
1.0.0 (source: target metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

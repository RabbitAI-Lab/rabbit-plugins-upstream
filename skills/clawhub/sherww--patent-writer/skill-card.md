## Description: <br>
Chinese-language patent disclosure drafting assistant that helps an agent research prior art, identify invention points, draft structured patent materials, create a proposal summary, and export Markdown or DOCX deliverables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Sherww](https://clawhub.ai/user/Sherww) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, inventors, and patent-support teams can use this skill to guide an agent through Chinese patent disclosure drafting from either a broad technical direction or a concrete invention idea. It supports prior-art research, invention-point refinement, section-by-section drafting, architecture diagram guidance, proposal summaries, and document export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The DOCX helper script can execute unintended local commands if crafted filenames or output paths reach its shell evaluation step. <br>
Mitigation: Review the script before use, restrict inputs to simple trusted filenames and output paths, and replace shell evaluation with a direct pandoc invocation before relying on DOCX export. <br>
Risk: Patent drafting may involve confidential invention details that could be exposed during external literature or web searches. <br>
Mitigation: Avoid entering confidential invention details into external search tools unless approved for that disclosure context, and review all generated prior-art claims against trusted sources. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/Sherww/patent-writer) <br>
- [Patent disclosure template](references/template.md) <br>
- [Writing guide](references/writing-guide.md) <br>
- [Architecture diagram guide](references/architecture-guide.md) <br>
- [Proposal summary template](references/proposal-summary-template.md) <br>
- [Proposal summary example](references/proposal-summary-example.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, files, shell commands, configuration] <br>
**Output Format:** [Markdown patent disclosure text, Markdown proposal summaries, SVG architecture diagrams, and optional DOCX files produced through pandoc.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill expects iterative user confirmation while drafting sections and depends on trusted local filenames and pandoc for DOCX export.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Creates evidence-based, management-ready workplace presentation decks from user-provided knowledge-base materials, work records, project files, meeting notes, resumes, spreadsheets, images, drafts, and corporate PowerPoint templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bz-ai](https://clawhub.ai/user/bz-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and workplace contributors use this skill to turn personal knowledge bases and company templates into report, promotion, probation, project, review, planning, and resource-request presentations with evidence tracking, staged confirmation, speaker notes, and slide-level quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect relevant workplace, resume, and knowledge-base files when those materials are made available for report generation. <br>
Mitigation: Keep unrelated personal or confidential files out of the active workspace, redact unnecessary sensitive identifiers, and review the generated SPEC and outline before PPTX creation. <br>
Risk: Generated report content could overstate achievements, blend current progress with completed results, or include unsupported business value claims. <br>
Mitigation: Use the evidence map, fact-status labels, data-gap list, and staged user confirmations before treating content as slide-ready. <br>
Risk: Generated PPTX files can contain layout errors, template drift, hidden metadata, or visible statements that were not intended for the audience. <br>
Mitigation: Render and inspect every slide, preserve confirmed template constraints, and verify that visible pages, notes, hidden objects, and document properties do not add unwanted attribution or sensitive content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bz-ai/skills/zhichang-shuzhi-ppt-assistant-codex) <br>
- [Evidence, fact status, and strategic SPEC](artifact/references/evidence-and-spec.md) <br>
- [Quality and delivery checks](artifact/references/quality-and-output.md) <br>
- [Report page contracts](artifact/references/report-page-contracts.md) <br>
- [Slide design and geometry rules](artifact/references/slide-design.md) <br>
- [Template page contract](artifact/references/template-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown planning artifacts, slide content specifications, speaker notes, source and checklist tables, and optional PPTX files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses staged user confirmation before outline generation and before PPTX creation; final delivery may include data-gap, source, placeholder, risk-expression, and visual-inspection checklists.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

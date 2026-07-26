## Description: <br>
Gdt Checker helps engineers review GD&T annotations on mechanical drawings for completeness and standards alignment, producing checklists and issue lists that identify missing annotations, datum-system errors, and symbol misuse. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Design, manufacturing, quality, and dimensional engineers use this skill to review GD&T information on 2D drawings, supplier drawings, drawing conversions, and FAI preparation materials. It produces an annotation-level checklist and issue list, while leaving final design and approval decisions to responsible engineering reviewers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users could treat the GD&T checklist as formal engineering approval. <br>
Mitigation: Require review and sign-off by the responsible design, manufacturing, or quality engineer before drawing release or supplier approval. <br>
Risk: Drawings and dimensional requirements may contain sensitive business or design information. <br>
Mitigation: Handle drawings under the organization's data-classification policy and avoid sharing confidential inputs with unapproved systems. <br>
Risk: The inspected artifact references a report-rendering script that was not included. <br>
Mitigation: Verify the installed release includes the expected report-generation assets, or use the generated text and Markdown guidance directly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-gdt-checker) <br>
- [Server-resolved GitHub repository](https://github.com/duding-engicool/skill-gdt-checker) <br>
- [Server-resolved GitHub commit](https://github.com/duding-engicool/skill-gdt-checker/commit/c96b6a2f74af783cd3ea4a1fd9dcf5f1ef294d36) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Plain text and Markdown checklists with issue lists, severity notes, and recommended corrections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Flags uncertain drawing context as pending confirmation and asks targeted follow-up questions when datum or functional requirements are missing.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Fill PDF forms programmatically with text values and checkboxes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[raulsimpetru](https://clawhub.ai/user/raulsimpetru) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to populate fillable PDF forms such as applications, surveys, and government forms with supplied text values and checkbox states. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF forms may contain sensitive personal, business, or government data. <br>
Mitigation: Use local copies of important PDFs and review the filled output before submitting or sharing it. <br>
Risk: Dependency behavior can vary across environments if pdfrw is resolved to different versions. <br>
Mitigation: Pin the pdfrw dependency in controlled environments. <br>
Risk: Some PDF viewers may not immediately show checkbox appearance changes even when values are set. <br>
Mitigation: Open and review generated PDFs in the intended viewer, such as Adobe Reader or Firefox, before relying on the visual result. <br>


## Reference(s): <br>
- [PDF Form Filler Examples](artifact/references/examples.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/raulsimpetru/skills/pdf-form-filler) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Files] <br>
**Output Format:** [Markdown with Python and shell examples; filled PDF files when executed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local PDF paths and caller-provided field data; no token-specific output constraints are stated.] <br>

## Skill Version(s): <br>
0.2.0 (source: frontmatter, setup.py, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

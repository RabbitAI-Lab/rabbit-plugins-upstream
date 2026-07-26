## Description: <br>
Organizes user-provided supplier Word, PDF, Excel, text, and Markdown materials into structured supplier quality management profiles with Markdown output and optional Word/PDF and SVG organization chart support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Supplier management, sourcing, and quality teams use this skill to convert supplied vendor records into a structured supplier quality dossier. It is intended for organizing provided materials, documenting quality certifications and processes, and producing review-ready profile files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Supplier records can contain confidential business, contact, quality, or audit information. <br>
Mitigation: Use the skill only with records you are authorized to process, store generated files in access-controlled locations, and delete local outputs when retention is no longer needed. <br>
Risk: Generated supplier profiles may preserve incomplete or uncertain source data as placeholders. <br>
Mitigation: Review the generated profile before relying on it for supplier qualification, audit, or quality management decisions. <br>
Risk: Optional Word/PDF and SVG generation depends on local Python tooling and conversion scripts. <br>
Mitigation: Verify local dependencies before requesting optional formats and keep the Markdown profile as the reviewable source artifact. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-supplier-profile-organizer) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-supplier-profile-organizer) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown supplier profile with optional Word/PDF files and SVG organization chart assets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May mark missing supplier fields as to-be-filled placeholders; Word/PDF output is optional.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

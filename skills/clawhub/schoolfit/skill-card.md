## Description: <br>
Use for Hong Kong school admissions, school selection, secondary school, primary school, kindergarten, international school, and postsecondary advisory workflows with SchoolFit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[djanngau](https://clawhub.ai/user/djanngau) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Families and education advisors use SchoolFit for Hong Kong school search, comparison, shortlisting, vacancy and admissions checks, and application-planning guidance across kindergarten, primary, secondary, international, and postsecondary options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live SchoolFit queries send school-selection preference text to schoolfit.hk and require a SchoolFit session access code. <br>
Mitigation: Disclose the remote query before live calls, keep the access code only in the active trusted chat or helper invocation, and never write the full code to logs, files, public docs, or final answers. <br>
Risk: User prompts may include student identity details or private family documents. <br>
Mitigation: Ask users to remove HKID, phone number, address, full student names, report-card files, and private document contents before any live SchoolFit API request. <br>
Risk: Vacancy and admissions information can become stale or be mistaken for a guarantee. <br>
Mitigation: Present vacancy and admissions data as time-limited leads and tell families to verify current status with the school or original notice. <br>


## Reference(s): <br>
- [ClawHub SchoolFit Page](https://clawhub.ai/djanngau/skills/schoolfit) <br>
- [SchoolFit Source Homepage](https://github.com/djanngau/schoolfit-skill) <br>
- [SchoolFit](https://schoolfit.hk/) <br>
- [SchoolFit Access Code](https://schoolfit.hk/skill-code) <br>
- [SchoolFit Applications](https://schoolfit.hk/applications) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with optional shell command examples and API-derived school-selection summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-oriented advisory output; live query responses should separate official facts, non-official band references, vacancy or admissions signals, and assumptions.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

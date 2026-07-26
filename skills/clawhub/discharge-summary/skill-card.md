## Description: <br>
Turn a hospital stay into a complete, well-structured discharge summary from provided hospital-course details, including admission reason, hospital course, diagnoses, procedures, discharge medications, condition, and follow-up or return precautions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinicians or authorized healthcare documentation users can use this skill to format supplied hospital stay details into a structured discharge summary for handoff and patient instructions. The treating clinician remains responsible for verifying all diagnoses, medications, pending results, follow-up, and return precautions before final use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive patient information supplied in conversation. <br>
Mitigation: Users should provide only patient information they are authorized to use and follow applicable privacy and security requirements. <br>
Risk: A generated discharge summary could contain incomplete or incorrect clinical details if source information is missing or ambiguous. <br>
Mitigation: A qualified clinician should verify the final summary, especially medications, diagnoses, pending results, follow-up plans, and return precautions. <br>
Risk: The skill is a documentation formatter and not a clinical decision tool. <br>
Mitigation: Use it to organize clinician-provided information only; do not rely on it for medical advice or for creating unsupported diagnoses, medications, doses, or results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/discharge-summary) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/discharge-summary.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown discharge summary with structured clinical sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes fields not documented and a clinician-review reminder; does not execute code or call tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Parse resumes and CVs (PDF, Word, images) into structured JSON profiles using SoMark for accurate document parsing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[soul-code](https://clawhub.ai/user/soul-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
HR teams, recruiters, and review agents use this skill to parse a user-selected resume or CV into local Markdown and JSON files, then produce a structured candidate profile and hiring assessment for review, comparison, or ATS workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume contents and extracted personal information are sent to SoMark for parsing. <br>
Mitigation: Confirm the user is comfortable sending the resume to SoMark before parsing and choose the intended regional endpoint. <br>
Risk: Parsed resumes and candidate data are saved locally as Markdown, JSON, and summary files. <br>
Mitigation: Use an output directory appropriate for sensitive candidate data and manage retention according to the user's data-handling requirements. <br>
Risk: The skill requires a SoMark API key and each parse consumes quota. <br>
Mitigation: Keep SOMARK_API_KEY in the environment rather than chat, confirm quota use before parsing, and run one parser invocation at a time for the same key. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/soul-code/skills/resume-parser) <br>
- [SoMark API endpoint, Mainland China](https://somark.cn/api/v1) <br>
- [SoMark API endpoint, outside mainland China](https://somark.ai/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, shell commands, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, local Markdown files, local JSON files, and a structured JSON candidate profile] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses one SoMark API call per parsed resume, writes parse_summary.json, and processes resumes one at a time for a given SOMARK_API_KEY.] <br>

## Skill Version(s): <br>
0.1.2 (source: evidence.release and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

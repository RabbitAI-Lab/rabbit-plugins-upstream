## Description: <br>
Review contracts and legal agreements in PDF, Word, and image formats for risks, unfair clauses, missing provisions, and key obligations using SoMark document parsing and structured AI-assisted risk analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[soul-code](https://clawhub.ai/user/soul-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, legal operations teams, procurement teams, and business reviewers use this skill to parse contract documents with SoMark and receive an AI-assisted report covering obligations, risk clauses, red flags, missing provisions, and recommended next steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected contract documents are sent to SoMark for parsing, which may expose confidential contract content to a third-party service. <br>
Mitigation: Use the skill only for contracts whose confidentiality rules allow third-party processing, and confirm the configured SoMark endpoint is the intended official regional endpoint before running. <br>
Risk: Each parse consumes one SoMark API call from the user's quota. <br>
Mitigation: Ask for explicit user confirmation before parsing and avoid parsing when saved Markdown or JSON outputs are not needed. <br>
Risk: The contract review is AI-assisted analysis and may not be suitable as binding legal advice. <br>
Mitigation: Present findings as review support and recommend consultation with a qualified attorney for binding legal decisions. <br>


## Reference(s): <br>
- [Contract Reviewer ClawHub Skill Page](https://clawhub.ai/soul-code/skills/contract-reviewer) <br>
- [SoMark API Endpoint - Mainland China](https://somark.cn/api/v1) <br>
- [SoMark API Endpoint - Outside Mainland China](https://somark.ai/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown contract review report, parser-generated Markdown and JSON files, and shell commands for SoMark parsing] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOMARK_API_KEY; parser output may include a Markdown contract file, a JSON parsed-contract file, and parse_summary.json.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

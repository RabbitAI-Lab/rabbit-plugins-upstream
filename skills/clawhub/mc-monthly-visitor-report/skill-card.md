## Description: <br>
Uses mc-cli to pull marketing cloud data and generate monthly real estate visitor analysis reports as HTML and PDF outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crespoyin](https://clawhub.ai/user/crespoyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Real estate marketing and sales teams use this skill to generate monthly site-visit analysis from project, customer, transaction, and recording transcript data. It supports management review, sales-team retrospectives, competitor analysis, consultant performance diagnosis, and follow-up planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can bulk export identifiable customer records and recording transcripts. <br>
Mitigation: Use only when authorized to process those records, restrict output locations, avoid broad sharing of raw transcripts and reports, and delete exported files when no longer needed. <br>
Risk: Generated reports and PDFs may contain customer names, phone fragments, or transcript excerpts. <br>
Mitigation: Redact customer names and phone fragments where possible before sharing reports outside the authorized team. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/crespoyin/skills/mc-monthly-visitor-report) <br>
- [Server-resolved GitHub provenance](https://github.com/crespoyin/mc-monthly-visitor-report) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, generated analysis files, HTML report, and PDF report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project information Markdown, customer details Markdown, transcript text files, a management HTML report, and a PDF report.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

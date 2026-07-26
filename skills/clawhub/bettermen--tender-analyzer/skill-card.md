## Description: <br>
Analyzes tender and bid documents, structures requirements with a MECE framework, simulates expert review scoring, proposes revisions, and can produce reports and version snapshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid, proposal, and procurement teams use this skill to parse tender files, organize requirements, estimate scoring risk, and prepare revision guidance. It is intended for workflows involving local bid documents that may contain sensitive commercial content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read sensitive tender or bid files and create local report or version artifacts. <br>
Mitigation: Use it only in approved workspaces, confirm output paths before running revision or version-management flows, and avoid sharing generated artifacts without review. <br>
Risk: Generated HTML reports can embed document-derived tender text as active browser content. <br>
Mitigation: Treat generated HTML as untrusted until document-derived fields are escaped or sanitized, and review reports before opening or distributing them. <br>
Risk: AI-estimated scores and revision suggestions may be incomplete or misleading for formal procurement decisions. <br>
Mitigation: Have qualified bid, legal, and procurement reviewers verify scoring assumptions, mandatory requirements, and proposed changes before submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/tender-analyzer) <br>
- [MECE multi-dimensional analysis framework](references/mece_framework.md) <br>
- [Bid scoring standards](references/bid_scoring_standards.md) <br>
- [Bid terminology](references/bid_terminology.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis, structured requirement tables, JSON-like records, SVG/HTML report content, and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read PDF, DOCX, XLSX, text, or Markdown bid materials and may save local HTML reports or version snapshots when helper scripts are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

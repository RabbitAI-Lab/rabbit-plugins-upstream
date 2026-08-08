## Description: <br>
Resume Styles Kit helps an agent create and optimize PDF-ready resumes from a candidate's real experience using five skills-section styles while preserving project detail, avoiding invented claims, and supporting batch HTML-to-PDF workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yll-kb](https://clawhub.ai/user/yll-kb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers, career-support agents, and resume writers use this skill to structure, style, and verify resume content before producing PDF-ready HTML variants. It is intended for workflows where the candidate supplies real experience data and reviews final output before sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume workflows can expose personal information when real candidate data is used. <br>
Mitigation: Decide up front whether the run should use real resume data or placeholder data; keep files local unless an external service is intentionally chosen, and review generated HTML/PDF files before sharing. <br>
Risk: The skill asks the agent to strengthen resume language, which could lead to overstated or unsupported claims if source data is incomplete. <br>
Mitigation: Use only candidate-provided experience, metrics, companies, projects, and technologies; ask for clarification before adding missing details. <br>
Risk: Resume content may be truncated or simplified during styling or PDF conversion. <br>
Mitigation: Check project order, bullet counts, page count, and pagination behavior before delivery, especially when generating multiple style variants. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yll-kb/skills/resume-styles-kit) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/yll-kb) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML, CSS, Python, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of local HTML and PDF resume files; generated content should be reviewed before sharing.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

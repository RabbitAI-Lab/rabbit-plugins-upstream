## Description: <br>
Analyzes plant images or videos to identify phenological features, classify the current growth stage, return confidence, and provide general stage-level care guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and smart-growing operators use this skill to analyze plant media from smart pots, grow boxes, greenhouses, or plant factories and obtain a structured growth-stage assessment with confidence and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provided plant media or URLs may be sent to Life Emergence cloud services for analysis and report generation. <br>
Mitigation: Use only images, videos, and URLs approved for third-party cloud processing; avoid sensitive locations, people, or confidential growing operations in submitted media. <br>
Risk: The skill can silently create or reuse an internal identity and persist account tokens locally. <br>
Mitigation: Run it in an isolated workspace or account context, review local data storage after use, and remove stored identity or token files when persistence is not desired. <br>
Risk: Cloud report-history queries may return account-linked analysis records. <br>
Mitigation: Limit installation and execution to users who are authorized to access the associated report history. <br>


## Reference(s): <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis content, confidence details, report links, and optional history tables.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the rendered result to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

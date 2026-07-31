## Description: <br>
Analyzes plant leaf images, videos, or URLs to identify likely nutrient deficiencies, confidence, fertilization direction, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit plant leaf media for nutrient-deficiency diagnosis and retrieve structured cloud analysis results. It is intended for gardening, greenhouse, planter, and plant-factory workflows where users need a likely deficiency class and practical next-step guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, or URLs are sent to a cloud analysis service. <br>
Mitigation: Use only media that may be shared with the service, avoid sensitive background content, and confirm any retention or deletion expectations before deployment. <br>
Risk: The skill automatically creates or reuses an identity and stores service tokens in a local SQLite database. <br>
Mitigation: Run in a controlled environment, restrict filesystem access to token storage, and rotate or remove stored credentials when the skill is no longer needed. <br>
Risk: Cloud report history can be retrieved for the associated identity without clear user confirmation. <br>
Mitigation: Require user confirmation before history retrieval in agent workflows and review returned reports before sharing them further. <br>
Risk: Nutrient-deficiency results may be uncertain or incomplete, especially when symptoms resemble plant disease or when image quality is poor. <br>
Mitigation: Treat outputs as decision support, verify with plant species context and soil testing, and consult an agricultural expert before applying specific treatments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Structured text or JSON rendered in Markdown, with optional saved report files and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report-history listings and exported report image links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server-resolved release metadata; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

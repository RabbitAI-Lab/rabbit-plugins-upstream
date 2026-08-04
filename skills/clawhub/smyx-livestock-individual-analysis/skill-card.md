## Description: <br>
Identifies individual livestock (pigs, cattle, sheep) by facial or body-pattern features and outputs a stable individual ID with confidence for precision farm management and tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit livestock images, videos, or URLs for individual animal identification, history report lookup, and precision farm tracking workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Livestock images, videos, or submitted URLs may be sent to the Life Emergence service for analysis. <br>
Mitigation: Obtain explicit user confirmation before upload and avoid submitting media that should not leave the user's environment. <br>
Risk: The skill can create or reuse a local identity, authenticate with the service, and store returned tokens in the workspace data database. <br>
Mitigation: Review token storage before installation and limit use to workspaces where local identity and service-token persistence are acceptable. <br>
Risk: The skill can query cloud history reports without clear user confirmation. <br>
Mitigation: Ask for explicit confirmation before listing history reports and review returned report links before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown or JSON text, with optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include individual IDs, confidence values, feature regions, analysis status, report links, and history tables.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; SKILL.md frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

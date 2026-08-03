## Description: <br>
Analyzes pet water-fountain video files or URLs through remote APIs to estimate drinking frequency, session duration, daily intake, historical changes, and alert-worthy changes without providing diagnosis or treatment advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze pet water-fountain area videos for structured drinking-behavior reports and history lookups. It is intended for pet health monitoring support, not veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded videos, supplied video URLs, report history queries, and managed identity data are sent to lifeemergence.com or open.lifeemergence.com services for processing. <br>
Mitigation: Use only when the user accepts remote cloud processing, avoid submitting sensitive media, and disclose that analysis and history retrieval depend on the remote service. <br>
Risk: The skill can silently create or reuse an identity and persist service tokens in the workspace database. <br>
Mitigation: Review the workspace data directory before and after installation, rotate or remove stored credentials when no longer needed, and install only in workspaces where this persistence is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and structured JSON returned from cloud analysis APIs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and historical report records from the remote service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

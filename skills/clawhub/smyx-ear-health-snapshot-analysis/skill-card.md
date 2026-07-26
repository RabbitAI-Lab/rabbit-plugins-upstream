## Description: <br>
Analyzes pet ear, head-shaking, or scratching media to produce visual ear-health observations, abnormality alerts, suggested owner or veterinary follow-up, and cloud report links without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, boarding centers, and pet-hospital intake teams use this skill to submit pet ear videos, images, local files, or URLs for structured visual observations of redness, discharge, earwax accumulation, and related risk prompts. The output is for health reference and pre-screening, not diagnosis or treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media, URLs, and report queries are sent to the LifeEmergence/SMYX cloud service. <br>
Mitigation: Use the skill only with media and URLs that are acceptable to process through that third-party service. <br>
Risk: The skill can create or reuse a workspace identity and persist local identity or token data. <br>
Mitigation: Use a dedicated workspace or account when possible, and review or remove smyx-api-key.txt and smyx-common-claw.db if identity reuse is not desired. <br>
Risk: The output is visual health reference material and may be mistaken for veterinary diagnosis. <br>
Mitigation: Treat findings as pre-screening observations and seek a veterinarian for medical diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown-style text containing structured JSON analysis, status messages, report-list output, and report export links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned analysis text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

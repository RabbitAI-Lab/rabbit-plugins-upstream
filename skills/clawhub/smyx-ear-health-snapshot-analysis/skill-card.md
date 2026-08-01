## Description: <br>
Analyzes pet ear, scratching, or head-shaking media to produce visual ear-health observations, abnormality alerts, suggested follow-up, and report links without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, boarding centers, and veterinary pre-screening teams use this skill to analyze pet ear images or videos for visual signs such as redness, discharge, suspected ear mites, and wax buildup. The skill returns structured observations, health-risk prompts, suggested follow-up, history listings, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet ear images, videos, or supplied URLs are sent to a configured cloud service for analysis. <br>
Mitigation: Use only media and URLs approved for cloud processing, and avoid private signed URLs or files containing household, owner, location, or other sensitive context unless that data handling is acceptable. <br>
Risk: The skill can create or reuse a local identity/token record and fetch cloud report history. <br>
Mitigation: Install it only in workspaces where persistent report access is expected, and review or clear local identity and token state according to operator policy before sharing or retiring the workspace. <br>
Risk: Visual ear-health observations could be mistaken for veterinary diagnosis or treatment advice. <br>
Mitigation: Present outputs as visual observations and follow-up suggestions only, and direct users to veterinary care for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown report or history table, with JSON available for detailed output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include visual observation summaries, abnormality alerts, owner check-up or veterinary visit suggestions, report links, and optional saved output files.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; SKILL.md frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

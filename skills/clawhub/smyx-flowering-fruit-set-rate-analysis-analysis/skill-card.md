## Description: <br>
Analyzes tomato or chili flower and fruit-cluster images or videos to count open flowers and young fruits, calculate fruit-set rate, and return practical pollination or growing-condition guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers and gardening agents use this skill to analyze tomato, chili, and similar fruiting-vegetable media for flower counts, young-fruit counts, and fruit-set rate. It is intended to support pollination checks, nutrition and environment review, and follow-up growing-condition adjustments without prescribing exact fertilizer or pesticide dosing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary reports that the skill sends plant images or videos and report queries to the configured LifeEmergence cloud service. <br>
Mitigation: Use only media that is appropriate to upload to that service, disclose the cloud processing path to users, and avoid submitting sensitive background content. <br>
Risk: The security summary reports that the skill creates or reuses a local identity and stores authentication tokens in a workspace SQLite database. <br>
Mitigation: Run it in a dedicated workspace, restrict workspace data access, and remove local identity or token storage before sharing the environment. <br>
Risk: The security verdict is suspicious and recommends review before installation. <br>
Mitigation: Review the skill package, token handling, and outbound service configuration before deploying it in shared or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-flowering-fruit-set-rate-analysis-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with counts, rate calculation, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return cloud report history and exported report URLs when the user requests prior analyses.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

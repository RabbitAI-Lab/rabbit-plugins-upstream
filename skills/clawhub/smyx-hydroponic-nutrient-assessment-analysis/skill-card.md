## Description: <br>
Assesses hydroponic plant root and leaf images or video to identify visual stress indicators, qualitatively judge nutrient solution concentration, and provide adjustment guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External hydroponic growers, plant factory operators, and developers use this skill to review root and leaf media for qualitative nutrient concentration status and directionally adjust dilution or nutrient supplementation. It is intended as visual support for cultivation decisions, not as a replacement for direct EC or ppm measurement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, and report-history requests may be sent to external cloud APIs for processing. <br>
Mitigation: Deploy only where cloud processing is acceptable, disclose upload behavior to users, and avoid submitting sensitive media. <br>
Risk: The skill may silently create or reuse an identity and store credentials or tokens locally. <br>
Mitigation: Review token storage and account-association behavior before deployment, restrict local file access, and rotate credentials if exposure is suspected. <br>
Risk: Visual assessment can provide misleading nutrient guidance because it does not measure EC or ppm directly. <br>
Mitigation: Treat outputs as cultivation guidance, confirm serious findings with direct measurements or expert review, and monitor plants after adjustments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis with report links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs qualitative visual findings, nutrient concentration status, adjustment advice, and optional cloud history-report listings.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

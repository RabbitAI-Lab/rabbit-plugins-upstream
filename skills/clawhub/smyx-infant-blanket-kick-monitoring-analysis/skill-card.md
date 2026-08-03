## Description: <br>
Identifies babies kicking off blankets or exposing their bodies during sleep and returns caregiver alerts, recommendations, structured reports, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and caregivers use this skill to analyze baby-room images, videos, or public media URLs for blanket-kicking or exposed-body events and to retrieve structured cloud reports or report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive baby-room images, videos, URLs, and report metadata may be sent to the Life Emergence cloud service. <br>
Mitigation: Use only with authorized media and explicit upload consent; review backend ownership, retention, access, and deletion controls before deployment. <br>
Risk: The skill can silently create or reuse local identity state and store access tokens for report retrieval. <br>
Mitigation: Run it in an isolated workspace, restrict access to local data files, clear token state when no longer needed, and confirm identity handling before enabling history lookups. <br>
Risk: The monitoring result is an auxiliary alert and may be incomplete or incorrect. <br>
Mitigation: Do not use the output as a substitute for caregiver supervision or a safe infant sleep environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-monitoring-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown or JSON analysis text, with optional saved output files and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local media files, public media URLs, cloud report history lookup, and documented mp4/avi/mov inputs up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact/SKILL.md frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

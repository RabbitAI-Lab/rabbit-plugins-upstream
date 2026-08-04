## Description: <br>
Identifies infant sleep states from baby-room monitoring media and generates structured sleep reports, schedule analysis, history listings, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers and agents use this skill to analyze infant sleep monitoring images, videos, or URLs for sleep state classification, sleep timing, wake counts, daily reports, and schedule insights. Developers may also use its CLI workflow to query cloud-hosted historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends baby-room media, image or video URLs, and report queries to cloud services. <br>
Mitigation: Install and run it only when the provider is trusted to process infant-monitoring media and sleep-report history. <br>
Risk: The skill silently creates or reuses an identity and may keep reusable identity or token records in the local workspace. <br>
Mitigation: Review local workspace storage and token handling before use, and clear persisted identity or token records when they are no longer needed. <br>
Risk: Sleep analysis results are for caregiver reference and may be unsuitable as medical advice. <br>
Mitigation: Treat reports as informational and consult a pediatric clinician for abnormal infant sleep patterns or health concerns. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Infant Sleep Monitoring API Documentation](artifact/references/api_doc.md) <br>
- [Shared Analysis API Error Codes](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown and JSON-like structured text, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return sleep analysis, historical report listings, and report export links; artifact documentation states mp4, avi, and mov inputs up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

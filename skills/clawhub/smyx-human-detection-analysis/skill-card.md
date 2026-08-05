## Description: <br>
Detects people in target areas from video files or URLs using computer vision and returns structured reports with counts, intrusion indicators, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to analyze surveillance video or image inputs for human presence, counts, repeated appearances, and intrusion indicators in parks, offices, and restricted areas. It can also retrieve cloud-hosted historical detection reports linked to the managed user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video or image files and URLs are uploaded to configured cloud APIs for analysis. <br>
Mitigation: Use only authorized footage, avoid sensitive surveillance media unless operators understand the upload path, and review the lifeemergence.com service terms and retention/deletion behavior before use. <br>
Risk: The skill silently creates or reuses local identity and token records for report association and history queries. <br>
Mitigation: Review local workspace data files such as smyx-common-claw.db and smyx-api-key.txt, and confirm operators understand how cloud reports are linked to the internally managed identity. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown reports and JSON structured results, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts a local video path or public video URL, optional detection-region coordinates, and a history-list mode that retrieves reports from the configured cloud API.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter states 1.0.13) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

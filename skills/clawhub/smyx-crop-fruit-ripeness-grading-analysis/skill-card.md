## Description: <br>
Identifies fruit ripeness stages from crop-fruit images or videos using color, size, and gloss cues, then returns a standardized ripeness grade. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, agricultural operators, and developers use this skill to grade tomato, pepper, and similar crop-fruit ripeness from media or URLs and to review report history for harvest-window decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crop images, videos, or submitted URLs are uploaded to configured LifeEmergence cloud services for analysis. <br>
Mitigation: Use only media and URLs approved for cloud processing; avoid private/internal URLs and files containing unrelated sensitive content. <br>
Risk: The skill may silently create or reuse an account-like identity and store returned service tokens locally. <br>
Mitigation: Review whether silent identity handling is acceptable before installation and confirm how local workspace data and tokens can be deleted. <br>
Risk: History-listing behavior retrieves cloud report history for the resolved identity. <br>
Mitigation: Confirm report-history retention and deletion expectations before using the skill with sensitive operational records. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown text containing structured JSON-style analysis and report links; optional local output file when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local file or URL input, report-history listing, and saved output files.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter is 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

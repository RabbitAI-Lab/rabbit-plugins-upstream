## Description: <br>
Analyzes plant images or videos to identify phenological features, classify the current growth stage, report confidence, and provide general care direction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and growers use this skill to analyze plant images or videos from smart pots, home grow boxes, greenhouses, or plant factories and receive a growth-stage classification with confidence and general care guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, and cloud report history may be processed by lifeemergence.com services under an implicit identity. <br>
Mitigation: Install only when that data flow is acceptable; prefer explicit confirmation for history lookup and documented retention and deletion practices. <br>
Risk: The skill can silently create or reuse an account and store tokens and profile-like fields locally. <br>
Mitigation: Review local credential storage, token rotation, and account creation behavior before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with JSON-style structured analysis, confidence information, report links, and optional saved result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [History lookup returns cloud report records; analysis accepts local files or public URLs for supported image and video formats.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Identifies fruit ripeness stages from crop fruit images or videos using color, size, and gloss features, then returns a standardized ripeness grade. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agricultural users and agents use this skill to grade ripeness for tomatoes, peppers, and similar crop fruit from images, videos, local files, or media URLs. It supports harvest-window decisions and historical report review through the configured cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fruit images, videos, or media URLs are sent to configured lifeemergence.com cloud services for analysis. <br>
Mitigation: Use only with media approved for that service, avoid unrelated sensitive content in captures, and review organizational data-sharing requirements before deployment. <br>
Risk: The skill can silently create or reuse an internal identity and store authentication tokens locally. <br>
Mitigation: Run the skill in a scoped workspace, review local data files periodically, and remove stored account or token data when persistent report history is not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON analysis report with ripeness grades, harvest-window guidance, and report links; optional saved text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Input may be a local image/video file path or a media URL; historical report listings are formatted as Markdown tables.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

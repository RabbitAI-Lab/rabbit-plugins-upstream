## Description: <br>
This skill analyzes plant images, videos, optional environmental data, and growth metrics through a cloud service to produce a 0-100 plant vitality score, vitality grade, trend, change percentage, alert hints, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to evaluate plant vitality from images, videos, optional environmental data, or growth metrics, especially for smart planters, plant factories, home gardening, and plant-monitoring platforms. It can also query prior cloud-generated vitality reports for the same resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, URLs, internal identifiers, and report history may be processed by the publisher's cloud service. <br>
Mitigation: Use the skill only with media, URLs, and report data approved for external cloud processing. <br>
Risk: The skill can silently create or reuse an identity and store reusable service tokens in the local workspace data directory. <br>
Mitigation: Run it in a controlled workspace, restrict access to local data files, and rotate or revoke tokens if that workspace is shared or exposed. <br>
Risk: Remote API calls upload local files or submit URL inputs with limited user control. <br>
Mitigation: Review inputs before execution and run the skill only in environments where outbound requests to the publisher service are expected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Plant vitality API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown-like status text with JSON-formatted structured analysis results or history records; optional file output when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results can include vitality scores, grades, trends, change percentages, alert hints, sub-scores, and report export links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

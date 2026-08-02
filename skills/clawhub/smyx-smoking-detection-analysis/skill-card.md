## Description: <br>
Automatically detects smoking behavior in target areas based on computer vision; supports real-time detection of video streams, images, and video files; identifies violation smoking behavior and triggers violation alerts, assisting in smoking control safety management for parks/communities/units. | 公共场所吸烟行为智能检测技能，基于计算机视觉自动检测目标区域内的吸烟行为，支持视频流、图片、视频文件实时检测，识别违规吸烟行为，触发违规预警，助力园区/社区/单位控烟安全管理 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external operators, and developers use this skill to analyze public-place images, video files, or video URLs for smoking behavior and receive structured detection reports, alerts, recommendations, and report links. It also supports querying cloud-hosted historical smoking-detection reports associated with the managed user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images, videos, or media URLs are sent to remote analysis services and may contain sensitive surveillance footage. <br>
Mitigation: Use only approved media, avoid sensitive footage where possible, and require explicit confirmation before the first upload. <br>
Risk: The skill silently creates or reuses a managed identity and can persist account tokens for later use. <br>
Mitigation: Run in a separate workspace, review local identity and token storage before installation, and remove stored credentials when the skill is no longer needed. <br>
Risk: Broad automatic triggers can retrieve account-linked historical reports from the cloud. <br>
Mitigation: Require explicit user confirmation before history retrieval and avoid exposing report history in shared sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance, configuration] <br>
**Output Format:** [Markdown text with structured JSON report content, status messages, Markdown tables, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write the returned report text to a caller-specified output file; media analysis supports local files or URLs and defaults to JSON detail.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter states 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

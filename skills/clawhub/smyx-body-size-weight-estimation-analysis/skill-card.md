## Description: <br>
Estimates livestock body length and body weight from side-view videos or frames, tracking fattening progress in a contactless manner. | 通过视频视觉估测体长、体重，追踪育肥进度。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to estimate livestock body measurements, body weight, fattening stage, and report links from side-view livestock images, videos, or URLs. It supports historical report lookup through the provider's cloud API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Livestock media and report history may be processed by the provider's cloud service. <br>
Mitigation: Use the skill only with media appropriate for provider processing, and avoid content that reveals sensitive farm layouts, people, location details, or confidential operations unless the provider's data handling is acceptable. <br>
Risk: The skill can automatically create or reuse a local identity and store reusable service tokens in the workspace data directory. <br>
Mitigation: Run it only in trusted workspaces, review local data-directory handling, and remove stored identity or token files when they are no longer needed. <br>


## Reference(s): <br>
- [API 接口文档](references/api_doc.md) <br>
- [API接口文档](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [JSON or Markdown report text with measurement estimates, fattening stage, and report links; optional file output is supported.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote provider API for analysis and historical report lookup.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; SKILL.md frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

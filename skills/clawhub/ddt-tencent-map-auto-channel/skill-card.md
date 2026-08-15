## Description:

使用腾讯地图中复制的地点名称和地址文本，基于店店通已发布门店快照分析汽车后市场品牌规模、省市覆盖、服务类型与竞争格局。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Automotive aftermarket market, channel, and site-planning teams use this skill to assess chain brand coverage, service-type mix, location context, and competitive presence from published DDT snapshots and user-provided map address text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive API credentials or location-related queries could be exposed if the skill is run in an uncontrolled environment.

Mitigation: Configure DDT_API_KEY only in a controlled runtime and avoid including secrets in prompts, logs, generated output, or version control.

Risk: Readers could mistake this for an official Tencent Map product or assume Tencent supplies the underlying data.

Mitigation: Preserve the artifact's disclosure that the skill is not affiliated with Tencent Map and that conclusions come from published DDT snapshots.

Risk: Limited snapshots, missing coverage, or truncated previews could be overread as complete market evidence.

Mitigation: Report coverage and data-version context, mark unavailable fields as not covered, and do not infer trends or complete market lists from limited previews.

## Reference(s):

- [DDT ClawHub homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-auto-channel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, and limited store details when explicitly requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a DDT_API_KEY and should not output secrets, storage IDs, supplier fields, or unsupported metrics.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

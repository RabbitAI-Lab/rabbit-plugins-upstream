## Description:

用 Cue 穿透人物的全生命周期工商与司法轨迹，剔离当前在册与历史风险，映射其商业控制版图，并产出可用于 IPO 或重大交易的个人背调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Deal, IPO, compliance, and executive diligence teams use this skill to organize public business, judicial, administrative-penalty, and affiliation records for a named person into a reviewable background-check workpaper. The output is a drafting aid that should be checked by qualified reviewers before use in formal decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill relies on an externally sourced, unpinned Cue runner that was not included in the reviewed artifact.

Mitigation: Review the runner source and install process before use, and pin the runner to a trusted commit or signed release.

Risk: Cue API keys and generated background-check reports may contain sensitive information.

Mitigation: Store API keys and reports securely, restrict access to authorized users, and avoid exposing them in prompts, logs, or shared workspaces.

Risk: Personal background checks can create legal and consent obligations.

Mitigation: Use the skill only for lawful, consented public-record checks where applicable, and require professional review before formal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-person-background-check)
- [Cue sample report](https://cuecue.cn/share/UvXieGTT)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [China Enforcement Information Disclosure](https://zxgk.court.gov.cn)
- [National Enterprise Credit Information Publicity System](https://www.gsxt.gov.cn)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Structured Markdown background-check workpaper with source links and optional conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and external Cue runner; results depend on public data source availability and should be professionally reviewed.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

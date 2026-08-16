## Description:

用 Cue 穿透人物的全生命周期工商与司法轨迹，剥离当前在册与历史风险、映射其商业控制版图，产出可用于 IPO 或重大交易的个人背调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to run Cue-powered public-record background-check workflows for IPO director and executive checks, major transaction diligence, partner onboarding, and senior candidate screening. The generated draft organizes identity, business roles, investments, judicial risks, administrative penalties, related companies, and source links for professional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends the target person's query to Cue's external API.

Mitigation: Confirm trust in the Cue runner and Cue service before use, and avoid submitting information unless the user has authority to process it.

Risk: Background-check reports can affect employment, credit, IPO, or transaction decisions.

Mitigation: Follow applicable consent and privacy requirements and obtain professional review before relying on the draft for formal decisions.

Risk: The draft depends on public records, Cue service availability, and external data-source freshness.

Mitigation: Review source links, rerun health checks when service errors occur, and verify material findings against authoritative public sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-person-background-check)
- [Cue report example](https://cuecue.cn/share/UvXieGTT)
- [Cue service](https://cuecue.cn)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [China Enforcement Information Disclosure Network](https://zxgk.court.gov.cn)
- [National Enterprise Credit Information Publicity System](https://www.gsxt.gov.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown background-check draft with command-line invocation and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saves a local Markdown report and may be converted to Word or PDF with pandoc.]

## Skill Version(s):

1.0.3 (source: evidence.release.version; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

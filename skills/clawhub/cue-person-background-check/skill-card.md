## Description:

使用 Cue 整理人物的公开工商、司法和行政处罚记录，形成供 IPO 或重大交易尽调使用的个人背调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

尽调人员和企业团队可用它整理候选人、管理人员或交易对手关键人物的公开工商、司法和处罚记录，并核查其关联企业与历史风险。底稿需经专业人士复核，不应直接作为最终决策依据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads an external runner that may change after installation.

Mitigation: Install only if you trust Cue and the runner; review or pin the runner before execution where possible.

Risk: A stored Cue API key could be exposed or misused.

Mitigation: Have the user create and manage the key, keep it protected, and never include it in reports or messages.

Risk: Personal background checks may be inappropriate without a lawful basis or required consent.

Mitigation: Use only legally appropriate public records, obtain subject consent when required, and have a professional verify sources before consequential use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-person-background-check)
- [Cue service](https://cuecue.cn/)
- [Cue runner (GitHub)](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror (Gitee)](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown background-check draft with public-source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a Cue report link when a report is available; may be converted to Word or PDF.]

## Skill Version(s):

1.0.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

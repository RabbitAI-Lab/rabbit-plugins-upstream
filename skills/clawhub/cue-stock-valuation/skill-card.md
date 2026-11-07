## Description:

用 Cue 对个股进行全周期估值分析——融合短线资金流向与中长线估值模型，短期看情绪博弈与支撑压力，中长期看业绩兑现与安全边际。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要研究个股或检查持仓的用户，生成短、中、长期估值与股价分析，涵盖资金面、业绩展望、估值模型和安全边际。结果用于研究参考，不构成具体买卖建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share an API key in chat.

Mitigation: Use protected local secret configuration instead of pasting the key into chat, and rotate any key already shared there.

Risk: The skill's prescribed flow restricts cancellation and requires promotional credit prompts.

Mitigation: Keep cancellation available and make credit promotions optional.

Risk: The external runner and service are not fixed by this package, and research runs consume account credits.

Mitigation: Review and pin the external runner before execution; make users aware that research queries go to Cue and runs consume account credits.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-stock-valuation)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-stock-valuation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Structured Markdown report with an executive summary, short-term market analysis, longer-term valuation analysis, source links, and risk notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research results depend on Cue and its external data sources; reported source links should be retained when available.]

## Skill Version(s):

1.0.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

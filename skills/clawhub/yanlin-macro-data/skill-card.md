## Description:

Collects macro liquidity indicators such as rates, foreign exchange, selected overseas market data, and representative U.S. equity quotes, with teaching snapshot fallbacks when live public data is unavailable.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts can use this skill for course-oriented macro-market data demonstrations and quick liquidity snapshots. Its outputs should be treated as teaching material and cross-checked before financial or operational use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Macro values may be stale, incomplete, or based on built-in teaching snapshots when public data is unavailable.

Mitigation: Check the output date and source labels, and verify numbers against authoritative market data before relying on them.

Risk: The evidence flags data-quality inconsistencies, including unsupported northbound-flow behavior.

Mitigation: Do not use the output for investment decisions; treat northbound-flow examples as unsupported unless the publisher fixes the documentation and implementation mismatch.

Risk: The skill makes public network requests to Sina Finance when live quotes are attempted.

Mitigation: Install and run it only in environments where outbound public finance-data requests are acceptable, and expect fallback behavior when requests fail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanlin-macro-data)
- [Sina Finance market data](https://finance.sina.com.cn)
- [Sina Finance futures quote endpoint](https://hq.sinajs.cn/list=hf_CL,hf_GC)

## Skill Output:

**Output Type(s):** [text, json]

**Output Format:** [Plain text summary or JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the run date and may include live public quotes or built-in teaching snapshot values depending on network availability.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

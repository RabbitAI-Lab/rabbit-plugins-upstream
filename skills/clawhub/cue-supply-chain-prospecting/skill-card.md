## Description:

用 Cue 沿核心企业客户、供应商和招投标关系链挖掘产业链上下游可拓展名单，并给出每家企业的切入点和可能的金融需求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External business development and corporate banking users use this skill to start from a core company and obtain a structured prospecting list across customers, suppliers, tender relationships, entry points, inferred financial needs, priority tiers, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, prospecting context, and a Cue API key are sent to cuecue.cn and an external runner that is not bundled in the reviewed artifact.

Mitigation: Install only after confirming this external data flow is acceptable for the intended use case and environment.

Risk: The skill steers insufficient-credit cases toward invitation or paid subscription flows and can weaken user control over cancellation, summarization, and reruns.

Mitigation: Keep the user in control of retries, cancellation, summarization, and any payment or invitation decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-prospecting)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with source links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated report should include the Cue original report link when a real conversation ID is returned.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

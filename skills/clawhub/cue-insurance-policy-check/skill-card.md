## Description:

用 Cue 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失，与同类产品客观对比，产出一份可向客户如实说明的条款理解底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance sales, compliance, and product teams use this skill to generate a structured policy-understanding draft for reviewing coverage, exclusions, waiting periods, rates, surrender loss, peer-product differences, and compliant customer-facing explanations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance prompts and Cue API credentials are sent to an external Cue service.

Mitigation: Avoid including personal customer data, policyholder identifiers, confidential business documents, or secrets unless Cue's privacy and retention terms are acceptable.

Risk: The generated policy analysis may be affected by Cue service availability and the freshness or availability of external sources.

Mitigation: Review the Markdown report against primary policy documents, cited sources, and applicable regulatory references before using it with customers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-insurance-policy-check)
- [Cue sample insurance policy check report](https://cuecue.cn/share/1c3d67d8bc4c)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [China Banking and Insurance regulatory source](https://www.cbirc.gov.cn)
- [Insurance Association of China](https://www.iachina.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key; report quality and freshness depend on Cue service availability and external data sources.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

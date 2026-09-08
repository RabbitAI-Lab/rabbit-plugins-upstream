## Description:

用 Cue 沿核心企业客户/供应商/招投标关系链，挖掘产业链上下游可拓展名单，给出每家切入点和可能的金融需求，助力对公客户经理精准拓客。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Corporate banking relationship managers and business development teams use this skill to start from a core company and ask Cue for upstream and downstream prospect lists, relationship context, entry points, financing needs, priorities, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business research queries and prospect context are sent to Cue's remote service.

Mitigation: Use only non-sensitive company names unless internal approval covers sending the research query and related business context to Cue.

Risk: The documented health check can expose a local Cue API key through command-line process metadata on shared or monitored systems.

Mitigation: Avoid running the curl health check with a real API key on shared systems; rotate the key afterward if exposure is possible.

Risk: The skill relies on an external Cue runner before producing reports.

Mitigation: Inspect the external Cue runner source before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-supply-chain-prospecting)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Example Cue report](https://cuecue.cn/share/Ml8DOQg5)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance, Business research guidance]

**Output Format:** [Markdown report with command-line snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a core company query, Cue API key, and template ID template_AKRtET; optional post-processing can convert Markdown reports to Word or PDF.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

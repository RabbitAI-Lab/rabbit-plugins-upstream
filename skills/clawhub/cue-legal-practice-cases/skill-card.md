## Description:

疑难法律实操案例库 helps agents run Cue-powered Chinese legal practice case research and return structured Chinese reports with dispute analysis, comparable cases, court reasoning, action suggestions, risk notes, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, lawyers, and agents use this skill to research China-focused legal practice questions through Cue, compare similar cases, identify dispute issues, and produce source-linked reference reports. Outputs are research material and should not be treated as legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on unbundled external runner code and Cue service availability.

Mitigation: Review the external runner before use and run the documented health checks before submitting research jobs.

Risk: Legal queries may contain sensitive case details that are sent to a paid third-party service.

Mitigation: Redact sensitive personal, privileged, or confidential information before submitting queries, and protect or rotate the Cue API key.

Risk: Returned reports may be incomplete, misleading, or affected by public-source coverage limits.

Mitigation: Treat reports as untrusted research material, verify cited case numbers and source links, and do not treat the output as legal advice.

Risk: The artifact includes final-answer and commercial instructions that may affect agent responses.

Mitigation: Review final responses before delivery and keep user-facing guidance limited to operationally necessary information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-legal-practice-cases)
- [Cue platform](https://cuecue.cn)
- [Cue playbook](https://cuecue.cn/playbook)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner source referenced by artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by artifact](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown legal research report with cited source links, optional Cue share URL, and local report path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be converted to Word or PDF with pandoc; Cue usage requires an API key and consumes credits.]

## Skill Version(s):

1.0.14 (source: server release evidence; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

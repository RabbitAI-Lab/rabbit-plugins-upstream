## Description:

站在指定一方立场逐条审查合同条款，核验主体与效力瑕疵、钱货闭环、违约责任与管辖约定，并输出带风险分级和修改建议的排查表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External legal, procurement, business, and compliance users use this skill to review uploaded contracts from a designated party's perspective and receive a risk-graded checklist with clause-level findings, citations, and directly usable revision suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive, confidential, or regulated contract content may be uploaded to Cue for analysis.

Mitigation: Use only when authorized to send the contract to Cue and when retention, access, and deletion terms are acceptable; avoid privileged, trade-secret, or highly confidential contracts unless approved.

Risk: The workflow asks users to provide and persist an API key.

Mitigation: Use a secure secret store where available, avoid pasting long-lived keys into chat, and rotate any key that may have been exposed.

Risk: The setup flow may run unpinned code from external repositories.

Mitigation: Review and pin the external runner source before execution, and run it with the least privileges needed for the contract-review task.

Risk: The generated contract report may be mistaken for formal legal advice.

Mitigation: Treat outputs as review assistance and have a qualified lawyer perform final review before signing or relying on the contract.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-contract-risk-review)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue service home](https://cuecue.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with risk-graded tables, legal citations or case identifiers, revision suggestions, setup commands, and a Cue share link when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a contract file or pasted contract text, the user's review posture, a Cue API key, and use of an external Cue runner; generated reports should not be treated as final legal advice.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

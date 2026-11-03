## Description:

围绕一个主题检索主要法域的公开判例与监管公告，归纳诉因、判决倾向与对中国主体的合规启示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要评估境外诉讼、制裁或监管风险的企业、合规人员及研究者，检索公开案例与公告，并整理诉因、判决趋势及合规启示。

### Deployment Geography for Use:

Global; documented coverage focuses on the United States, European Union, Singapore, and selected public regulatory sources.

## Known Risks and Mitigations:

Risk: A Cue API key or local configuration file could be exposed.

Mitigation: Use a dedicated API key configured locally, protect the configuration file, and do not paste the key into chat.

Risk: Installing and automatically running an unpinned external runner may execute code that has not been reviewed.

Mitigation: Review the runner, use a fixed version, and retain control over stopping jobs.

Risk: Research questions are sent to Cue and may contain confidential information; runs also consume credits.

Mitigation: Assess confidentiality and expected credit use before submitting a question.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-overseas-litigation)
- [Cue Playbook](https://cuecue.cn/playbook)
- [PACER](https://pacer.uscourts.gov)
- [Court of Justice of the European Union (CURIA)](https://curia.europa.eu)
- [OFAC Sanctions List Search](https://sanctionssearch.ofac.treas.gov)
- [BIS Entity List](https://www.bis.gov/entity-list)
- [ICSID Cases](https://icsid.worldbank.org/cases)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Chinese Markdown report with case summaries, legal grounds, outcome trends, penalties or damages, compliance takeaways, and source links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage depends on publicly available sources; the artifact states that results are not legal advice.]

## Skill Version(s):

1.2.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

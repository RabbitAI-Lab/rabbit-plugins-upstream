## Description:

境外诉讼案例库围绕一个主题检索主要法域的公开判例与监管公告，并归纳诉因、判决倾向与对中国主体的合规启示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and legal or compliance teams use this skill to request Chinese-language research reports on overseas litigation, sanctions, regulatory actions, investment diligence, and intellectual-property disputes involving cross-border business topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal research prompts and the Cue API bearer key are sent to cuecue.cn.

Mitigation: Use the skill only for matters approved by the user's organization, and avoid privileged, confidential, or highly sensitive legal content unless that external service use is authorized.

Risk: The skill relies on an external Cue runner repository and remote Cue service availability.

Mitigation: Review the external runner before execution, run the documented health checks, and use the documented public-source fallback channels if Cue is unavailable.

Risk: Generated legal research may omit sources outside the covered public databases and does not constitute legal advice.

Mitigation: Verify cited sources, review coverage limits, and have qualified legal professionals assess decisions based on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-overseas-litigation)
- [Cue API key page](https://cuecue.cn/api-key)
- [Cue service health endpoint](https://cuecue.cn/api/health)
- [Cue playbook endpoint](https://cuecue.cn/api/playbook)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [PACER](https://pacer.uscourts.gov)
- [CURIA](https://curia.europa.eu)
- [OFAC sanctions search](https://sanctionssearch.ofac.treas.gov)
- [BIS Entity List](https://www.bis.gov/entity-list)
- [ICSID cases](https://icsid.worldbank.org/cases)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with source links and optional shell commands for setup, health checks, and format conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are saved locally under the user-specified output path; Word or PDF conversion is optional with pandoc.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

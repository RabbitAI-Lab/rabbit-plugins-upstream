## Description:

检索主要境外法域的公开判例与监管公告，并归纳诉因、判决倾向及对中国主体的合规启示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and legal or compliance teams use the skill to research overseas litigation and regulatory actions, summarize relevant cases and trends, and identify compliance considerations for Chinese entities. Its reports are research aids, not legal advice.

### Deployment Geography for Use:

Global, focused on overseas jurisdictions and public-source coverage.

## Known Risks and Mitigations:

Risk: The workflow installs and updates an external runner, so an unreviewed update could change behavior.

Mitigation: Use a reviewed, pinned runner revision and approve updates deliberately; keep the sandbox enabled.

Risk: The security evidence flags weak credential safeguards; the workflow uses a local Cue API key.

Mitigation: Protect the key directory and file with permissions 0700 and 0600, configure credentials locally, and do not send them in chat.

Risk: Research questions are sent to Cue, which may expose confidential matter details.

Mitigation: Consider confidentiality before submitting queries and avoid including sensitive information unless approved.

Risk: Research runs consume credits and may involve charges.

Mitigation: Confirm research charges before use and retain cancellation control.

## Reference(s):

- [Cue platform](https://cuecue.cn/)
- [Cue Playbook](https://cuecue.cn/playbook)
- [PACER](https://pacer.uscourts.gov)
- [Court of Justice of the European Union (CURIA)](https://curia.europa.eu)
- [OFAC Sanctions List Search](https://sanctionssearch.ofac.treas.gov)
- [BIS Entity List](https://www.bis.gov/entity-list)
- [ICSID Cases](https://icsid.worldbank.org/cases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Chinese Markdown research report with source links; case names and legal provisions may retain their original language.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage depends on available public sources and varies by jurisdiction; reports are not legal advice.]

## Skill Version(s):

1.2.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

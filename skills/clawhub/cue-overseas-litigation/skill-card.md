## Description:

检索主要法域的公开判例和监管公告，并归纳诉因、判决倾向及对中国出海主体的合规启示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

For legal, compliance, and research teams assessing overseas litigation and regulatory risks. Users can investigate a topic across major jurisdictions and receive a Chinese report summarizing cases, claims, outcomes, compliance implications, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed when shared in chat.

Mitigation: Configure the key outside chat in an owner-only file and rotate any key already exposed.

Risk: The external runner and hosted service are outside the artifact's audit scope, and runner updates may change behavior.

Mitigation: Inspect and pin the runner, restrict its local access, and require deliberate approval for updates; preserve the ability to stop runs and decline promotions.

## Reference(s):

- [Cue Playbook](https://cuecue.cn/playbook)
- [Cue platform](https://cuecue.cn)
- [Cue runner source (as referenced by the skill)](https://github.com/sensedeal/cue-skills)
- [PACER](https://pacer.uscourts.gov)
- [CURIA](https://curia.europa.eu)
- [OFAC Sanctions List Search](https://sanctionssearch.ofac.treas.gov)
- [BIS Entity List](https://www.bis.gov/entity-list)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance, Shell commands, Configuration]

**Output Format:** [Chinese Markdown research report with source links, plus occasional shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports organize cases, claims, outcomes, penalties or damages, compliance implications, and source links; case names and legal provisions may retain their original language.]

## Skill Version(s):

1.2.10 (source: server-resolved release metadata; packaged artifact frontmatter says 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

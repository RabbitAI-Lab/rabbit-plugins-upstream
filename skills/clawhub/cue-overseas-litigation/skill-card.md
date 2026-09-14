## Description:

境外诉讼案例库 helps an agent research public overseas court cases and regulatory notices, then summarize causes of action, outcomes, penalties, compliance implications, and source links for China-facing cross-border matters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, compliance, and due-diligence users use this skill to request Chinese-language reports on overseas litigation, sanctions, export-control, intellectual-property, and regulatory matters involving companies or industries. It is intended for research support from public sources, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external runner that the security evidence describes as unpinned.

Mitigation: Use a pinned or otherwise verified runner version before deployment.

Risk: The skill stores a Cue API key locally.

Mitigation: Treat the API key as a secret and restrict permissions on ~/.cue/config.json.

Risk: Legal research queries are sent to Cue's service.

Mitigation: Avoid confidential or privileged facts in prompts unless the user or organization has approved that data sharing.

Risk: Reports are generated from public-source coverage and may be incomplete for some jurisdictions or non-public disputes.

Mitigation: Review the cited source links and use qualified legal review before relying on conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-overseas-litigation)
- [Cue API key](https://cuecue.cn/hub/api-key)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [PACER](https://pacer.uscourts.gov)
- [CURIA](https://curia.europa.eu)
- [OFAC Sanctions Search](https://sanctionssearch.ofac.treas.gov)
- [BIS Entity List](https://www.bis.gov/entity-list)
- [ICSID Cases](https://icsid.worldbank.org/cases)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with source links and optional conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are saved to a local Markdown path and depend on Cue service availability, API key validity, credits, and public-source coverage.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

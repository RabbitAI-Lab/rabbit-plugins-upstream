## Description:

境外诉讼案例库 helps an agent use Cue to research public overseas litigation, regulatory notices, sanctions and export-control records, and cross-border legal risk, returning sourced Chinese Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, compliance, and cross-border business users can use this skill to ask an agent for overseas litigation and regulatory-risk research around a company, industry, technology area, sanction, export-control issue, or public case pattern. The skill is suited to preliminary research and source gathering, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User queries may contain privileged, personal, or commercially sensitive legal facts that would be sent to Cue's external service.

Mitigation: Redact sensitive details before use and submit only queries approved for external processing.

Risk: The skill can consume Cue credits when running a research job.

Mitigation: Confirm credit availability and expected consumption before starting the job.

Risk: The research depends on Cue and public source availability, so results may be delayed, incomplete, or marked unavailable.

Mitigation: Run the documented health checks first and verify important conclusions against the cited source links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-overseas-litigation)
- [Cue API key page](https://cuecue.cn/api-key)
- [Cue health endpoint](https://cuecue.cn/api/health)
- [Cue playbook endpoint](https://cuecue.cn/api/playbook)
- [PACER](https://pacer.uscourts.gov)
- [CURIA](https://curia.europa.eu)
- [OFAC Sanctions Search](https://sanctionssearch.ofac.treas.gov)
- [BIS Entity List](https://www.bis.gov/entity-list)
- [ICSID Cases](https://icsid.worldbank.org/cases)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with source links and optional shell commands for setup, health checks, and format conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are generated through the external Cue service and may be saved to a local Markdown file.]

## Skill Version(s):

1.2.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

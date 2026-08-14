## Description:

事实核查 helps an agent use Cue to cross-check claims against independent sources and underlying data, then produce a structured fact-checking report with source comparisons and correction evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to fact-check research notes, news claims, diligence materials, and market rumors by sending the claim text or link to Cue for multi-source verification and evidence-backed correction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted documents, private URLs, secrets, or regulated data may be sent to Cue and related external data sources.

Mitigation: Do not submit confidential or regulated content unless the user is comfortable sending it to those external services.

Risk: Cue API keys may be exposed through local configuration or logged health-check commands.

Mitigation: Protect the Cue API key and avoid running credential-bearing checks in shared or heavily logged environments.

Risk: The skill depends on an external Cue runner and Cue service availability.

Mitigation: Review the external runner source before installation, run the documented health checks, and retry or use the documented manual alternatives when Cue or upstream sources are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fact-check)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue service](https://cuecue.cn)
- [Example fact-checking report](https://cuecue.cn/share/680abf29664d)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and optional shell commands for Cue execution and format conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include claim-by-claim conclusions, correction evidence, independent source comparison, discrepancy analysis, and source links.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Automates Amazon product opportunity scans for sellers by selecting strategies, validating candidates with ZooData data, and ranking opportunities by a composite score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiclaw](https://clawhub.ai/user/apiclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and commerce analysts use this skill to discover candidate products, compare market signals, and plan follow-up validation before investing in inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a ZooData API key and may also read an optional local ZooData credential file.

Mitigation: Prefer the ZOODATA_API_KEY environment variable, keep the key scoped to ZooData use, and remove unused persistent local credentials.

Risk: Broad opportunity scans can consume paid API credits.

Mitigation: Review the estimated credit cost and confirm before running multi-call scans; use granular or quick-scan commands when working under a credit cap.

Risk: Product recommendations are based on sampled marketplace data and may be incomplete or time-sensitive.

Mitigation: Treat reports as decision support, validate promising products with additional sources, and avoid acting solely on a generated ranking.

Risk: The skill performs external API calls and local CLI execution.

Mitigation: Use the bundled command allowlist, verify network requests are limited to trusted ZooData hosts, and inspect command parameters before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-opportunity-discoverer)
- [Publisher profile](https://clawhub.ai/user/apiclaw)
- [Project homepage](https://github.com/SerendipityOneInc/ZooData-Skills)
- [ZooData API Field Reference](references/reference.md)
- [ZooData CLI Contract](references/cli-contract.md)
- [ZooData API keys](https://zoodata.ai/en/api-keys)
- [ZooData pricing](https://zoodata.ai/en/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with tables, CLI command examples, data provenance, and API usage summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should match the user's language and label conclusions by confidence when presenting sampled API data.]

## Skill Version(s):

1.0.9 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps Amazon sellers use ARI review data to generate VOC reports, identify customer pain points and buying motives, compare competitors, monitor negative-review alerts, and turn review language into Listing titles, bullets, A+ copy, keywords, and operational recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to analyze collected Amazon review samples, generate customer-voice reports, and convert those findings into Listing optimization and operations guidance. It is intended for users who want ARI's full review operations workflow, including paid analysis, exports, alerts, and monitoring controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI workflows can spend credits.

Mitigation: Review or disable auto-confirm, check quoted credit cost and balance, and require explicit confirmation before paid actions unless the user has set a clear auto-confirm policy.

Risk: The skill can change ongoing monitoring, watch, schedule, and competitor settings.

Mitigation: Confirm the exact ASIN, site, schedule, competitor, and cost impact before making account-monitoring changes.

Risk: A saved ARI API key can access the connected ARI account until it is revoked.

Mitigation: Store the key only in the local ARI configuration or environment, never include it in reports or examples, and revoke it from ARI if exposed.

## Reference(s):

- [ARI CLI 与 API 参考](references/reference.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/listing-optimizer)
- [ARI Product Site](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and links; some workflows can export CSV, Markdown, or HTML through ARI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on ARI API responses and available Amazon review samples; paid workflows may return report IDs, report URLs, credit usage, and current balance.]

## Skill Version(s):

1.4.5 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

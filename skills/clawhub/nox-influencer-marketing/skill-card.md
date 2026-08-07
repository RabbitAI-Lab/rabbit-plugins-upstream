## Description:

Runs NoxInfluencer creator and marketing-ops workflows via CLI for influencer marketing, creator marketing, UGC, social media marketing, and affiliate marketing, including creator discovery and result exports; evaluation; external contacts; known-video and future-content monitoring; spreadsheet imports/reports; campaigns, collections, CRM, product center, short links, Shopify affiliation, email/message tasks, files, brand monitoring, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noxinfluencer](https://clawhub.ai/user/noxinfluencer)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams and agents use this skill to find, evaluate, contact, monitor, and manage creators through NoxInfluencer. It supports creator discovery, campaign operations, CRM and outreach workflows, exports, brand monitoring, quota checks, and account setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a NoxInfluencer account, including outreach, CRM, campaign, export, contact retrieval, unlock, and upload workflows.

Mitigation: Install it only when account operation is intended, and review sensitive actions before approval.

Risk: Approved actions can consume Skill quota, SaaS-side entitlements, contact quota, or paid membership capabilities.

Mitigation: Check quota and pricing before broad searches, exports, unlocks, or contact retrieval.

Risk: Email or message sends, scheduled outreach, and CRM or campaign mutations can affect live marketing operations.

Mitigation: Use dry-run, validate, preview, and explicit approval gates before executing writes.

Risk: Some platform data is partial or platform-limited, especially Instagram audience detail, TikTok and Instagram cooperation data, and brand-monitor product signals outside YouTube.

Mitigation: Surface unavailable fields plainly and avoid confident recommendations when critical data is missing.

Risk: Chinese-site routing changes the service endpoint and URLs used by the workflow.

Mitigation: Confirm Chinese-site routing with the user before using the Chinese-language route.

## Reference(s):

- [NoxInfluencer Skills](https://www.noxinfluencer.com/skills)
- [Marketing Ops Workflows](artifact/references/marketing-ops.md)
- [Brand Monitor Workflows](artifact/references/brand-monitor.md)
- [CLI Response Format](artifact/references/cli-response-format.md)
- [Platform Support](artifact/references/platform-support.md)
- [Search Filter Semantics](artifact/references/search-filters.md)
- [Verdict Heuristics Reference](artifact/references/verdict-heuristics.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, text]

**Output Format:** [Concise natural-language summaries with agent-executed CLI actions and file paths for approved exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or download files, queue exports, modify NoxInfluencer resources, consume quota, or send approved outreach when the user authorizes those actions.]

## Skill Version(s):

0.1.17 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

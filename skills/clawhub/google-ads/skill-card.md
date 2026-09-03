## Description:

Query, audit, and optimize Google Ads campaigns using an attached browser or the Google Ads API, with read-only reporting by default and bounded approval required before account changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to inspect Google Ads performance, investigate campaign, keyword, budget, conversion-tracking, and wasted-spend questions, and prepare reviewed account-change proposals when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may access sensitive Google Ads account data and locally configured advertising credentials.

Mitigation: Keep credentials in protected local configuration, do not paste secrets into chat, and report only scoped account findings without exposing credential values.

Risk: Incorrectly scoped or premature edits could change campaigns, bids, budgets, targeting, labels, or conversion settings.

Mitigation: Keep activity read-only unless the user explicitly requests a change, then require an exact bounded preview, action-time approval, and post-write readback.

Risk: Recommendations based on incomplete context could mislead advertising decisions.

Mitigation: Confirm account identity, date range, business objective, conversion actions, and relevant uncertainty before making recommendations.

## Reference(s):

- [Google Ads API Start Guide](https://developers.google.com/google-ads/api/docs/start)
- [Google Ads API Release Notes](https://developers.google.com/google-ads/api/docs/release-notes)
- [Google Ads API Upgrade Guide](https://developers.google.com/google-ads/api/docs/upgrade)
- [Google Ads API Client Libraries](https://developers.google.com/google-ads/api/docs/client-libs)
- [Google Ads API Limits and Quotas](https://developers.google.com/google-ads/api/docs/best-practices/quotas)
- [Google Ads API Read and Reporting Reference](references/api-setup.md)
- [Google Ads Attached-Browser Workflows](references/browser-workflows.md)
- [Google Ads Mutation Workflow](references/mutation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with evidence tables, inline code or shell snippets, and bounded approval previews for requested account changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to read-only reporting; account changes require exact before-and-after preview approval and post-change readback.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

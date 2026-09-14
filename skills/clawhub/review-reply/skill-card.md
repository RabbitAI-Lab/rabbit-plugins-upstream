## Description:

Review Reply helps Amazon sellers inspect subscribed ASIN reviews, triage negative reviews, draft buyer replies, prepare appeal language, identify product improvements, and generate ARI review-analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to work with ARI on subscribed ASIN reviews: identifying negative-review drivers, drafting response and appeal guidance, generating VOC and operations reports, comparing competitors, and monitoring product or review changes. It requires an ARI API key and can interact with ARI account credits according to service-side confirmation rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits under server-side auto-confirm rules.

Mitigation: Use the documented quote-only or always-ask posture before paid actions, and review costs before allowing confirmed credit-spending commands.

Risk: The skill handles Amazon review and account-related data through ARI.

Mitigation: Install only when the user trusts ARI for that data, and avoid placing API keys or account secrets directly in chat.

Risk: Export actions can overwrite local files when directed to existing filenames.

Mitigation: Use export destinations intentionally and avoid existing filenames unless overwriting is expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-reply)
- [README](artifact/README.md)
- [User guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown, with optional CLI command guidance and report/export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ARI review summaries, negative-review triage, response and appeal drafts, product-improvement recommendations, VOC or operations report summaries, and credit/confirmation status.]

## Skill Version(s):

1.4.11 (source: server evidence, frontmatter, _meta.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

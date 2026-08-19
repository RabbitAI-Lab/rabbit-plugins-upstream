## Description:

Analyzes Amazon keyword traffic sources for competing ASINs, including organic search, Sponsored Products, Sponsored Brands, video ads, recommendation placements, Amazon's Choice, editorial recommendations, and top-rated exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce analysts, and agents use this skill to query LinkFox SIF keyword data and compare which ASINs receive traffic for a keyword through organic, paid, and recommendation channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends keyword queries and API credentials to LinkFox services.

Mitigation: Use only approved LinkFox credentials and avoid submitting confidential keywords or account data unless the user accepts that disclosure.

Risk: Onboarding can request phone/SMS login information and initiate payment flows.

Mitigation: Prefer a preconfigured API key; use phone login or payment commands only after explicit user consent.

Risk: Full API responses and cache files may persist under linkfox/ session directories.

Mitigation: Review stored files after use, avoid shared workspaces for sensitive analyses, and delete cached or response files when no longer needed.

Risk: Feedback submission behavior may include business or conversation details.

Mitigation: Do not submit feedback automatically without consent, and redact sensitive details before any report is sent.

Risk: Each uncached request consumes LinkFox credits and repeated parameter changes can increase cost.

Mitigation: Confirm before repeated calls, reuse the 24-hour cache when appropriate, and explain expected credit usage before continuing.

## Reference(s):

- [SIF Keyword Traffic API Reference](artifact/references/api.md)
- [LinkFox Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-keyword-summary)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, shell command examples, and JSON API responses or saved JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large API responses are summarized in stdout while the full response is saved under a linkfox/ session data directory; repeated identical requests may use a 24-hour cache.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps users set up, improve, audit, debug, and plan analytics tracking for marketing and product measurement across tools such as GA4, Google Tag Manager, Mixpanel, Segment, and UTM-based campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[coreyhaines31](https://clawhub.ai/user/coreyhaines31)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and product teams use this skill to create tracking plans, define event taxonomies, configure GA4 and GTM, debug broken or duplicate analytics events, and plan privacy-aware measurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analytics examples can lead to collection of personal data, secrets, sensitive URLs, or free-text error details if copied into production without review.

Mitigation: Review tracking payloads before deployment, avoid PII and secrets, use pseudonymous identifiers, and redact free-text fields or URLs that may contain sensitive data.

Risk: GA4, GTM, Google Ads, Facebook Pixel, or similar tags may fire before users provide required consent.

Mitigation: Gate analytics and marketing tags on appropriate consent, use consent mode or a consent management platform, and confirm regional privacy obligations before launch.

## Reference(s):

- [Event Library Reference](artifact/references/event-library.md)
- [GA4 Implementation Reference](artifact/references/ga4-implementation.md)
- [Google Tag Manager Implementation Reference](artifact/references/gtm-implementation.md)
- [Google Analytics recommended events](https://support.google.com/analytics/answer/9267735)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration]

**Output Format:** [Markdown with tables, checklists, and inline JavaScript or tag configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tracking plans, event/property taxonomies, UTM conventions, GA4 and GTM setup steps, debugging checklists, and consent or privacy reminders.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

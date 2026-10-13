## Description:

Checks whether AI answers cite a connected site using observed answers, AI crawler activity, referral visits, and published business facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[minh42](https://clawhub.ai/user/minh42)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners and marketing teams use this skill to see whether AI answers cite their site, which pages AI crawlers fetch and refer visitors to, and whether AI claims match their published business facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting SEOmatic exposes the site's citation, traffic, and analytics data to the connected service account.

Mitigation: Confirm the service is trusted and grant only the intended site access; prefer OAuth over a long-lived API key where available.

Risk: Missing observations or logged-out scans can be mistaken for evidence that real users never see citations.

Mitigation: Label observed and scanned results separately, and explain missing extension data rather than reporting zero citations.

## Reference(s):

- [SEOmatic AI Citations skill on ClawHub](https://clawhub.ai/minh42/skills/seomatic-ai-citations)
- [SEOmatic](https://app.seomatic.ai)
- [SEOmatic agent connection settings](https://app.seomatic.ai/dashboard/settings?tab=ai-agents)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes observed citations from logged-out scans and identifies gaps in citation, crawler, and referral data.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

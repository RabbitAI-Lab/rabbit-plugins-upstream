## Description:

Checks publicly accessible image URLs with LinkFox Ruiguan to identify similar registered copyrighted works and summarize similarity, rights-owner, TRO history, and radar infringement indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce sellers, designers, and their agents use this skill to assess image copyright risk before using product or design images. It provides factual risk indicators and should not be treated as legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs and local image files may be sent to LinkFox services, and local uploads become publicly accessible for about 24 hours.

Mitigation: Use only images acceptable for external processing; avoid confidential or unreleased assets unless that exposure is acceptable.

Risk: Phone-number login, OTP handling, API-key output, and payment QR flows are sensitive account and billing actions.

Mitigation: Prefer first-party account pages where possible, keep API keys in environment variables, and require user confirmation before billing or payment steps.

Risk: Detection results and caches may contain sensitive business data in local linkfox output or cache files.

Mitigation: Review and delete local linkfox output and cache files after use when results, image references, or account data are sensitive.

Risk: Service calls consume credits and repeated checks can create unexpected cost.

Mitigation: Warn users before additional calls, reuse cached results when appropriate, and avoid automatic retries or repeated queries without user consent.

Risk: Copyright matches are limited to the service database and are not legal conclusions.

Mitigation: Present findings as factual risk indicators and recommend qualified legal review for definitive copyright decisions.

## Reference(s):

- [睿观-版权检测 API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-copyright-detection)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API results saved to local files or printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write complete API responses and cache files under a local linkfox directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

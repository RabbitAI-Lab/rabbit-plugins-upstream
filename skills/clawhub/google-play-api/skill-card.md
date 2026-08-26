## Description:

Google Play helps agents query fetcher.sh for Google Play app search, app details, reviews, permissions, data-safety disclosures, similar apps, and developer catalogs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover Android apps, inspect app metadata, review user feedback, compare similar apps, and support ASO or competitor-monitoring workflows without Google Play Console access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls to the third-party fetcher.sh API may spend prepaid credits or x402 payments.

Mitigation: Confirm payment posture before use, monitor balance or settlement requirements, and avoid unintended paid calls.

Risk: Bearer credentials can authorize paid API access if exposed.

Mitigation: Keep FETCHER_API_KEY private, avoid committing it to files, and rotate it if exposure is suspected.

Risk: The artifact states that upstream failures are not refunded after settlement.

Mitigation: Use low-volume test calls first and account for non-refundable settled requests in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/google-play-api)
- [Server-resolved GitHub source](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/google-play)
- [Full agent setup](https://googleplay.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://googleplay.fetcher.sh/openapi.json)
- [Condensed catalog](https://googleplay.fetcher.sh/llms.txt)
- [Google Play fetcher site](https://googleplay.fetcher.sh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [External API responses use JSON with status, message, and data fields; paid calls require prepaid credits or x402 payment.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

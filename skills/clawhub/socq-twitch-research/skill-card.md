## Description:

Research public Twitch content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to collect and analyze public Twitch profile and recorded-video data through SocQ while preserving endpoint choice, credit estimates, pagination state, task status, and collection caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests are credit-metered and large or repeated Twitch collections can consume credits or encounter API-key rate and credit limits.

Mitigation: Read endpoint billing details, report expected cost, confirm before paid large-volume or multi-endpoint runs, and use API-key credit and rate controls where available.

Risk: SOCQ_API_KEY exposure could allow unauthorized SocQ-authenticated requests.

Mitigation: Keep the key in the environment, avoid putting it in prompts, URLs, committed files, or retained commands, and use IP allowlists or credit limits for sensitive environments.

Risk: Twitch research results can be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report collection time, pages read, whether more data remains, failed requests, unsupported filters, and any incomplete coverage.

Risk: Running the latest CLI package through npx may be unsuitable for sensitive environments.

Mitigation: Use a reviewed or pinned socq CLI installation when stronger change control is required.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platforms](https://socq.ai/platforms)
- [Twitch API Documentation](https://docs.socq.ai/api-manual/twitch)
- [SocQ MCP and CLI](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Twitch Profile Endpoint](https://docs.socq.ai/api-manual/twitch/profile)
- [Twitch User Videos Endpoint](https://docs.socq.ai/api-manual/twitch/user-videos)
- [Async Tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Errors and Recovery](references/errors.md)
- [Pagination and Files](references/pagination.md)
- [Twitch Platform Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, command examples, task status, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates, pagination status, collection timestamps, incomplete-coverage notes, and unsupported-filter notes.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

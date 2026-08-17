## Description:

Research public keyword volume, suggestions, related terms, difficulty, intent, organic results, and site rankings with SocQ for SEO discovery, endpoint selection, credit estimates, asynchronous execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and SEO analysts use this skill to collect and compare public SEO metrics through SocQ while controlling endpoint choice, pagination, asynchronous task status, and credit usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests use API keys, network calls, and credit-metered execution.

Mitigation: Keep SOCQ_API_KEY in the environment or CLI config, review expected credit usage before larger runs, and do not place API keys in prompts, URLs, shell history, or committed files.

Risk: Large-volume or multi-endpoint research can spend credits or return incomplete coverage when pagination, provider failures, or unsupported filters occur.

Mitigation: Confirm scope and expected cost before paid runs, preserve task IDs, follow pagination, and label incomplete coverage or unsupported filters in the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-seo-research)
- [SocQ developer tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ SEO API documentation](https://docs.socq.ai/api-manual/seo)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SEO endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, credit usage, task status, pagination state, normalized findings, or raw export location.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

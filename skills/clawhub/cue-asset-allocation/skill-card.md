## Description:

Generates a monthly Cue-powered asset-allocation report that combines macro indicators, policy and liquidity context, and stock, bond, and commodity allocation rationale into a client-ready Markdown brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Financial advisors, investment committee contributors, and portfolio analysts use this skill to run a Cue-powered monthly macro asset-allocation workflow and produce a client-ready report covering allocation logic, ratios, risks, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Cue API keys and report queries to the external Cue service.

Mitigation: Install and run it only when the user accepts Cue as an external service provider and has reviewed API key handling expectations.

Risk: The workflow depends on an external runner and Cue service availability.

Mitigation: Review the runner source before execution and run the documented health checks before starting report generation.

Risk: Generated asset-allocation reports may be mistaken for independent financial advice.

Mitigation: Present reports as advisory material and require human investment review before using them with clients or committees.

Risk: The skill includes Cue share, referral, and payment links in some user-facing flows.

Mitigation: Make those links transparent to users and avoid presenting payment or referral prompts as required unless the Cue service reports insufficient credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-asset-allocation)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue payment page](https://cuecue.cn/pay)
- [Cue runner source cited by artifact](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror cited by artifact](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with setup and execution commands, a Cue share link when available, and a local report path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and external Cue service availability; reports should be treated as advisory material, not independent financial advice.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Aggregates customs trade intelligence, global company due-diligence data, and LinkedIn professional-network data to support B2B prospecting, supplier validation, market sizing, and cross-border lead generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, sourcing, export, and B2B prospecting teams use this skill to analyze product markets, profile companies and trade partners, identify decision-makers, and map professional networks before outreach or due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles paid external API calls.

Mitigation: Tell the user that calls incur fees, confirm before fee-bearing operations, and use the skill's price-info flow rather than estimating costs.

Risk: The skill processes personal contact and professional-network data.

Mitigation: Use it only for lawful B2B research and avoid retaining or sharing personal data beyond the user's approved purpose.

Risk: The UpKuaJing API key is stored locally and used for authenticated requests.

Mitigation: Protect the API key file, do not expose secrets in prompts or logs, and rotate the key if it may have been disclosed.

Risk: Task outputs and logs may contain sensitive business or personal data.

Mitigation: Avoid verbose logs when possible and delete task_data outputs and logs when they are no longer needed.

Risk: Security evidence reports under-disclosed update/version checks.

Mitigation: Review network behavior before installation or deployment and account for update checks in security review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/b2b-lead-generation)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Skill API references](artifact/references/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command invocations and JSON API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, httpx, and an UPKUAJING_API_KEY; API calls are fee-bearing and may write task_data outputs.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

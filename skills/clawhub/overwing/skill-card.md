## Description:

Helps agents screen text for safety and sensitive information, identify AI bot User-Agent claims, and submit governed actions to business systems through Overwing Tower.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frod27](https://clawhub.ai/user/frod27)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use Overwing to check messages before sending or acting on them, assess AI crawler identity claims, and route authorized business-system changes through Tower for execution or human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checked text and Tower action payloads are sent to Overwing.

Mitigation: Send only data approved for this service and avoid including unnecessary sensitive content.

Risk: Exposed API or agent keys could allow account access or business-system actions.

Mitigation: Keep OVERWING_API_KEY and OVERWING_AGENT_KEY secret and grant Tower agents only the scopes they need.

Risk: Tower submissions may change business records or require human approval.

Mitigation: Prefer dry-run or decide before writes, and do not bypass a pending human review.

Risk: The optional MCP install path invokes an unpinned package.

Mitigation: Pin or review the overwing-mcp package before using npx.

Risk: Automated safety verdicts are signals rather than guarantees.

Mitigation: Involve a human for consequential decisions, especially when the recommended action is not allow.

## Reference(s):

- [Overwing skill on ClawHub](https://clawhub.ai/frod27/skills/overwing)
- [Overwing agent guide](https://overwing.ai/llms.txt)
- [Overwing API documentation](https://overwing.ai/docs)
- [Overwing Atlas](https://overwing.ai/atlas)
- [Overwing Tower](https://overwing.ai/products/tower)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text guidance and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evaluation verdicts include recommended actions and per-rule results; Tower actions return decisions, statuses, and receipts.]

## Skill Version(s):

1.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

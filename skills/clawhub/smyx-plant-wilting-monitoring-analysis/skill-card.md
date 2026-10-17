## Description:

Analyzes plant images or videos for signs of wilting and provides monitoring reports and early-warning guidance through a cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and plant-care teams use the skill to assess wilting in plant photos or videos, receive early-warning reports, and review previous monitoring results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or media URLs are sent to the Life Emergence cloud service for analysis.

Mitigation: Use only media approved for cloud processing; seek clearer consent and retention controls before sending sensitive material.

Risk: The skill can silently create or reuse a local identity, register or log in, and persist service tokens in a workspace database.

Mitigation: Review account association and token deletion controls before installation, and restrict access to the workspace containing stored tokens.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes monitoring findings, suggestions, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

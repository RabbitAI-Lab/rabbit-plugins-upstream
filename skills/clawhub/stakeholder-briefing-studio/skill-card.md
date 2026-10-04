## Description:

Classifies stakeholder briefing material by audience and assembles a client-facing brief from eligible sections while recording omissions for internal follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Communications teams and account owners use this skill to select briefing sections appropriate for a stakeholder audience and prepare a preview for review before external circulation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A locally saved briefing preview may contain sensitive business material or be circulated before review.

Mitigation: Use a dedicated output directory for sensitive material and review the preview before sharing it externally.

## Reference(s):

- [Stakeholder Briefing Studio on ClawHub](https://clawhub.ai/wxt-ai/skills/stakeholder-briefing-studio)
- [Package README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [JSON response with an audience policy or briefing preview; downstream also writes a local Markdown outline]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The preview lists included and excluded sections; the downstream operation writes a local file only when invoked with an output directory.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

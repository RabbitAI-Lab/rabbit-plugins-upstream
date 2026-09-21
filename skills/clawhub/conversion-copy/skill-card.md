## Description:

Uses Amazon product-detail and review evidence to diagnose buyer decision barriers and suggest conversion-oriented listing copy; it is not for conversion-rate prediction, advertising, or automatic publishing and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to request evidence-based recommendations for improving listing conversion copy from product details and review signals. The skill guides the agent through ARI authorization, profile checks, quote confirmation, and generation of concise findings without modifying or publishing Amazon pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires trusting ARI with an API key and product or review data, and the key may be saved locally.

Mitigation: Review the skill before installing, use the documented ARI authorization flow, and configure credentials only in environments where local credential storage is acceptable.

Risk: Paid ARI credits can be spent after explicit confirmation.

Mitigation: Run quote or profile checks first, proceed only after the user explicitly confirms the quoted request, and use status checks rather than rerunning interrupted confirmed jobs.

Risk: The bundled CLI can run broader server-side product-operation workflows than the fixed conversion-copy workflow described by the skill.

Mitigation: Ensure agents use only the documented listing/conversion workflow, the ops_listing output template, and the commands described in artifact/references/operation-workflow.md.

## Reference(s):

- [Amazon Conversion Copy API Reference](artifact/references/reference.md)
- [Amazon Conversion Copy Operation Workflow](artifact/references/operation-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/conversion-copy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise findings, review evidence, conclusions, and inline bash commands when setup, quoting, or status checks are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Amazon ASIN and site, an ARI API key, and explicit user confirmation before paid collection or analysis runs.]

## Skill Version(s):

1.4.13 (source: evidence.release.version, artifact/_meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

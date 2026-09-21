## Description:

Checks an Amazon listing's mobile reading order, information density, and comprehension blockers using product-detail and review evidence; it does not cover ads, inventory, orders, profit, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and listing operators use this skill to inspect the mobile shopping reading path, identify evidence-backed comprehension issues, and request optimization guidance before making manual listing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI exposes workflow and focus overrides that could support broader product-operation analyses than the mobile-listing purpose promises.

Mitigation: Review before installing if a strictly narrow mobile-listing-only skill is required, and use only the documented listing/mobile operations flow.

Risk: The skill stores an ARI API key locally and can spend account credits for collection or analysis.

Mitigation: Run setup or configure only in a trusted environment, check account status, review the quote, and proceed only after explicit confirmation.

Risk: The skill sends product and review analysis requests to the third-party ARI service.

Mitigation: Use the documented https://ari.funewa.com endpoint only, do not bypass endpoint or redirect blocking, and avoid submitting data that should not be shared with that service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/mobile-listing)
- [README](artifact/README.md)
- [Amazon mobile listing API reference](artifact/references/reference.md)
- [Amazon mobile listing operation workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional inline shell commands and ARI service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis is quoted first and runs only after explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact _meta.json, CHANGELOG, and ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

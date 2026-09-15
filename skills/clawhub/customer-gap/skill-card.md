## Description:

Checks Amazon product-page promises against real customer review experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and agents use this skill to compare listing promises with customer review evidence before making product or listing decisions. It is not intended for Amazon policy review, legal compliance review, or unsupported marketing generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can be steered into other ARI operation workflows despite claiming a fixed audit/promise scope.

Mitigation: Use only the documented commands for the promise-audit workflow and avoid passing workflow or focus parameters unless the publisher fixes local contract enforcement.

Risk: Paid ARI actions can consume credits after quote confirmation.

Mitigation: Verify quotes and request IDs before confirming paid runs; when a run is interrupted, check status rather than directly rerunning a confirmed command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/customer-gap)
- [Amazon 消费者预期差距 API 参考](references/reference.md)
- [Amazon 消费者预期差距 专属运营工作流](references/operation-workflow.md)
- [ARI service origin](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands and JSON responses from the ARI CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis runs require quote review and explicit confirmation.]

## Skill Version(s):

1.4.11 (source: evidence.release.version, artifact/_meta.json, artifact/scripts/ari.py, artifact/CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

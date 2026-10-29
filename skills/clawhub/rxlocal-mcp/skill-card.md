## Description:

Read an RxLocal pharmacy patient portal account profile and account-holder age gate through a signed-in browser tab with the fpx CLI; prescription, refill, and pharmacy-message reads are currently unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

RxLocal and PioneerRx portal users can use the skill to read their account profile and age-gate status from a signed-in portal session. Developers can use its documented commands and response examples when working with those account reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw command accepts POST requests that could change pharmacy-account data, despite the skill's read-only positioning.

Mitigation: Use a corrected release limited to verified read operations. Avoid raw POST commands and require explicit approval before any account change.

Risk: Portal responses can contain personal or medical information, and the helper uses the signed-in account token.

Mitigation: Do not print or save the token. Pair only the intended browser, and protect any returned personal or medical information.

## Reference(s):

- [RxLocal endpoint catalog](artifact/references/endpoints.md)
- [RxLocal fpx recipes](artifact/references/recipes.md)
- [RxLocal patient portal](https://patient.rxlocal.com)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/rxlocal-mcp)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and Markdown documentation with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account profile and age-gate data are returned as JSON; unsupported portal reads report an error.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

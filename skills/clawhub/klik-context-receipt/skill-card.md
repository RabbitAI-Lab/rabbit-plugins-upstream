## Description:

Turn a short, redacted work update into a reviewable Context Receipt that records source, freshness, scope, authority, open questions, and a human-return condition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyixu](https://clawhub.ai/user/chengyixu)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users, developers, and teams use this skill to turn a redacted work update into a compact handoff receipt before resuming work, transferring context, or asking a person to review missing authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated receipt could be mistaken for approval to execute work or make commitments.

Mitigation: Treat the receipt as a review aid only; return to a person for new access, judgment, external commitments, or conflicting context.

Risk: Users could include sensitive or excessive source material in the work update.

Mitigation: Provide only short, redacted context and omit credentials, private transcripts, client data, financial information, health information, and other sensitive material.

Risk: The optional Klik link could be read as required operational context or validated product support.

Mitigation: Use the link only as optional marketing context; do not infer recorder, model, provider, tool, integration, or product support from the receipt.

## Reference(s):

- [Klik pre-launch direction](https://pre.hiklik.ai/?utm_source=clawhub&utm_medium=companion_skill&utm_campaign=kickstarter_prelaunch&utm_content=context_receipt)
- [ClawHub skill page](https://clawhub.ai/chengyixu/skills/klik-context-receipt)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Analysis]

**Output Format:** [Markdown receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Non-executing, redacted handoff structure for human review.]

## Skill Version(s):

1.0.0 (source: package.json and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

TextRazor provides actions for account and quota lookup, text analysis, classification, named-entity extraction, and management of custom classifiers and entity dictionaries through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate TextRazor from an agent workflow through the oo CLI. It supports natural-language processing tasks such as content analysis, classification, entity extraction, and managed updates to TextRazor custom classifiers or dictionaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may run remote installer scripts directly in a shell without verification.

Mitigation: Review the oo CLI installation path before installing, prefer official signed packages or verified downloads, and require explicit approval before setup commands.

Risk: Some TextRazor actions can remove or overwrite custom classifiers or entity dictionaries.

Mitigation: Confirm the target, payload, and intended effect with the user before running any action tagged as destructive.

Risk: Authentication, connection changes, and billing-related setup can affect the user's OOMOL or TextRazor account state.

Mitigation: Do not run login, connection, recharge, or setup commands proactively; run them only after a matching failure and with explicit user approval.

## Reference(s):

- [TextRazor homepage](https://www.textrazor.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-textrazor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return TextRazor connector JSON responses that include data and execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

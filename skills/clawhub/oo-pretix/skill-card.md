## Description:

pretix helps agents work with pretix organizers, events, items, and orders through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to inspect live pretix connector schemas and run pretix organizer, event, item, and order actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path recommends remote installer one-liners.

Mitigation: Prefer a pinned or signed official installer and verify it before execution.

Risk: pretix connector calls are mediated by OOMOL and can expose data available to the connected pretix account.

Mitigation: Install only for accounts where that data exposure is acceptable and confirm the connected account scope before use.

Risk: The security evidence notes confusing action labeling, including get_order behavior.

Mitigation: Confirm the exact payload and effect before running actions tagged as write or destructive, and clarify get_order behavior before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pretix)
- [pretix homepage](https://pretix.eu)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector responses in JSON when pretix actions are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

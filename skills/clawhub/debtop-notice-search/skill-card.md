## Description:

Searches and organizes public debt-notice records by enterprise, creditor, debtor, or topic keyword, returning notice lists, timelines, principal amounts, guarantor and collateral clues, and source-linked details from 智收云MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninjaliang](https://clawhub.ai/user/ninjaliang)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and due-diligence teams use this skill to search public debt transfer, disposal, solicitation, and collection notices, compare results, and summarize disclosed amounts, parties, guarantees, collateral, and detail links. It is intended for read-only public-notice research, not credit scoring or legal conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guest fallback contacts agent.debtop.com and stores guest.json plus device.id in the local cache.

Mitigation: Prefer a managed MCP/OAuth connector when available, and delete the local cache if guest session reuse is not desired.

Risk: Public notice data may be incomplete, stale, or ambiguous for similarly named entities.

Mitigation: Label the output as public-notice scope with query time, avoid creditworthiness or legal conclusions, and do not merge same-name entities without confirmation.

Risk: Repeated or concurrent searches can hit shared guest-session limits.

Mitigation: Keep calls serial with at least one second between tool calls, avoid bulk export, and stop paginating when upstream errors or timeouts occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ninjaliang/skills/debtop-notice-search)
- [Guest access reference](artifact/references/guest-access.md)
- [Tools and fields reference](artifact/references/tools-and-fields.md)
- [Error handling reference](artifact/references/errors.md)
- [Client source ID reference](artifact/references/client-source-ids.md)
- [Notice report template](artifact/templates/notice-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown report with tables, linked notice details, and concise guidance; helper scripts emit shell commands or plain-text token/link output when guest fallback is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public notice results; detail links should include a stable client source parameter, and missing fields should be labeled as undisclosed rather than inferred.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

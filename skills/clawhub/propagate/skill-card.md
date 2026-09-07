## Description:

Propose a canonical home, concrete consumers, and any justified runtime home for a reusable tool, library, skill, document, or workflow after building a reusable capability or when asked where it should live, with execution gated on approval of exact targets and actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill after creating or identifying a reusable capability to decide its canonical home, concrete consumers, integration form, and whether any runtime host is justified. It keeps distribution, ownership, authorization, and maintenance tradeoffs explicit before any copy, commit, publication, deployment, or infrastructure action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose cross-repository copies, publication, deployment, installation, or infrastructure actions that exceed the user's intended authorization.

Mitigation: Treat output as a proposal until the user approves exact targets and actions; verify source and destination state before executing any approved change.

Risk: A distribution review can expose private code, records, endpoints, credentials, or client context if the agent inspects beyond the authorized scope.

Mitigation: Inspect only repositories, records, and hosts already in scope; mark unknown inventories as unknown and avoid including sensitive material in proposals.

Risk: Installing or running the skill through an untrusted host or CLI can make the surrounding agent environment the effective trust boundary.

Mitigation: Install only through a trusted host or CLI and treat the skill as a planning aid unless exact execution actions are separately approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/propagate)
- [ClawHub publisher profile](https://clawhub.ai/user/antreasantoniou)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown proposal with concise action lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposal-first; exact copy, commit, publish, deploy, install, or infrastructure actions require separate user approval.]

## Skill Version(s):

1.0.0 (source: release evidence and CHANGELOG, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

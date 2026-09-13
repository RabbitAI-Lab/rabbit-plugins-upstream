## Description:

Query and manage OpenTable reservations from a shell with @fetchproxy/cli by routing one-shot GraphQL and REST calls through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-oriented users use this skill to search OpenTable restaurants, inspect availability, view reservations or favorites, and prepare fpx commands for booking, modifying, or canceling reservations through their own signed-in OpenTable session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated fpx commands can create, modify, or cancel OpenTable reservations without an enforced confirmation step.

Mitigation: Require a fresh human-readable preview and explicit confirmation before booking, modifying, canceling, or changing favorites.

Risk: The skill requires access to a signed-in OpenTable browser session.

Mitigation: Install only when the operator is comfortable granting the agent access to that session and its account data.

Risk: Example request bodies use fixed /tmp paths that may expose sensitive JSON or collide on shared systems.

Mitigation: Use private temporary directories or restricted-permission files for reservation, profile, card-token, and security-token data.

Risk: A globally installed or changing fpx CLI can alter request behavior over time.

Mitigation: Prefer a pinned local fpx installation for repeatable operation.

## Reference(s):

- [OpenTable request catalogue](references/opentable-fpx-requests.md)
- [Initial-state extractor](references/extract-initial-state.mjs)
- [OpenTable](https://www.opentable.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON request bodies, jq filters, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through the user's signed-in OpenTable browser session and can perform real account actions.]

## Skill Version(s):

0.19.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

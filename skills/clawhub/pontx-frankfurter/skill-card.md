## Description:

Maintain legacy Frankfurter v1 integrations through Pontx for existing v1 applications, reproducible dated reference-rate work, or decisions about moving provider-aware work to pontx-frankfurter-v2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to maintain Frankfurter v1 exchange-rate integrations, prepare reproducible reference-rate requests, preview live reads through Pontx, and evaluate migration to the v2 contract.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may retrieve live exchange-rate data or current Pontx contract details when explicitly asked.

Mitigation: Preview Pontx commands before execution, perform live reads only after an explicit user request, and recheck current metadata if authentication is required.

Risk: Frankfurter v1 behavior may be confused with v2 semantics or current-calendar-day assumptions.

Mitigation: Keep version-specific adapters separate, use explicit completed dates for reproducible reports, and surface conflicts between product guidance and the current Pontx contract.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and code-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Pontx preview or call commands and application-code integration guidance; live retrieval is gated by explicit user request.]

## Skill Version(s):

1.0.0 (source: release metadata and auto changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

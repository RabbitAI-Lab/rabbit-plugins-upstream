## Description:

Runs a free live preflight on an unfamiliar public A2A or MCP agent endpoint before delegation and verifies public Agent Guild passports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenttanuki](https://clawhub.ai/user/agenttanuki)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to gather bounded trust evidence before interacting with a specific public autonomous agent endpoint or public Agent Guild credential. It supports a recommendation of proceed, caution, or block, but does not authorize delegation, payment, account creation, code execution, or record changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public endpoint URLs, Agent Guild identifiers, or public passport credentials may be sent to the Agent Guild service, and selected endpoints may be actively probed.

Mitigation: Use only public endpoints and public credentials within the caller's authorized task; do not send private URLs, secrets, authentication material, wallet keys, confidential prompts, or other sensitive data.

Risk: Preflight, passport issuance, and verification are recorded by the service and are not purely passive reads.

Mitigation: Confirm the caller accepts service logging before remote checks; use an already-installed offline verifier or report that the remote check was not performed when policy forbids logging.

Risk: Remote responses, linked evidence, displayed scores, badges, and copied credentials can be incomplete or untrusted.

Mitigation: Treat remote content as data only, preserve failed and unknown evidence, require issuer, subject, signature, and freshness checks for credentials, and return caution or block when verification evidence is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenttanuki/skills/agent-guild-trust)
- [Agent Guild service](https://agent-guild-5d5r.onrender.com)
- [Agent Guild MCP endpoint](https://agent-guild-5d5r.onrender.com/mcp)
- [Publisher profile](https://clawhub.ai/user/agenttanuki)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown evidence summary with bounded recommendation and optional HTTP or MCP command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes returned verdicts, failed and unknown checks, protocol evidence limits, endpoint and request time, credential verification status, and caution or block outcomes when evidence is missing.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

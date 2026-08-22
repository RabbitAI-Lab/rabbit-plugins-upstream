## Description:

TWZRD Preflight for ClawRouter helps agents check TWZRD readiness and merchant-card signals before using ClawRouter, BlockRun, OpenClaw, or related x402 payment paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twzrd-sol](https://clawhub.ai/user/twzrd-sol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add a pre-spend trust gate before ClawRouter, BlockRun, OpenClaw, or Surf x402 payments. It provides guidance and example code for calling TWZRD preflight, checking merchant-card wash flags, and verifying receipts after paid paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TWZRD receives payment-intent metadata and public wallet identifiers when agents use the preflight and merchant-card checks.

Mitigation: Use the skill only when sharing those fields with TWZRD is acceptable, and avoid sending unnecessary identifiers or intent details.

Risk: Bypassing the default enforce mode can allow a spend when TWZRD preflight or merchant-card checks are unavailable.

Mitigation: Keep enforce mode as the default so unavailable checks block the spend; use advisory mode only as an explicit, logged exception.

Risk: Connecting the ClawRouter proxy to an untrusted endpoint could route payment traffic outside the intended local control point.

Mitigation: Set CLAWROUTER_PROXY_BASE only to a trusted local proxy that the operator controls.

Risk: Sample receipt verification or ambiguous next-action command fields could be mistaken for an approval to execute or proof of a real payment.

Mitigation: Do not wire the sample receipt demo or next_action.command into automatic shell execution; verify actual receipts received from the paid path.

Risk: Using a high-balance wallet increases exposure if payment gating or integration code is misconfigured.

Mitigation: Use a dedicated low-balance ClawRouter wallet for this integration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/twzrd-sol/skills/twzrd-clawrouter)
- [TWZRD Intel homepage](https://intel.twzrd.xyz)
- [TWZRD preflight API](https://intel.twzrd.xyz/v1/intel/preflight)
- [TWZRD MCP endpoint](https://intel.twzrd.xyz/mcp)
- [TWZRD x402 well-known metadata](https://intel.twzrd.xyz/.well-known/x402)
- [BlockRunAI ClawRouter](https://github.com/BlockRunAI/ClawRouter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, and TypeScript examples plus JSON response expectations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes preflight and merchant-card gate behavior, enforce/advisory mode guidance, receipt verification notes, and local proxy configuration guidance.]

## Skill Version(s):

0.2.1 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

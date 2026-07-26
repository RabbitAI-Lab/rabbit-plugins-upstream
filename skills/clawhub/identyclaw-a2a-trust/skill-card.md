## Description: <br>
Cryptographically trusted OpenClaw inter-agent messaging that wraps payloads in identyclaw.collaboration.v1 envelopes with HOLA mutual auth for sessions_send or A2A when messages need forged-sender protection or verifiable task delegation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[identyclaw](https://clawhub.ai/user/identyclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to build and verify trusted OpenClaw inter-agent messages for same-gateway sessions_send and internet A2A workflows. It helps receivers verify HOLA envelopes before executing delegated task payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: NEAR private keys, IdentyClaw JWTs, and Passport identifiers may be exposed if environment variables or credential files are shared too broadly. <br>
Mitigation: Keep credentials scoped and protected, avoid logging secrets, and review credential handling before installing or running the helper scripts. <br>
Risk: A verified envelope could be mistaken for broad authorization to execute any delegated task. <br>
Mitigation: Use HOLA verification only as an identity and delegation signal; retain normal task authorization, sandboxing, and approval checks before execution. <br>
Risk: Wire JWT claims, sender display names, or session labels may be confused with task identity. <br>
Mitigation: Verify the HOLA envelope and require the verified peerTokenId to match envelope.from.tokenId before trusting the task payload. <br>
Risk: The npm helper scripts depend on a local @rodit/hola-client package path that may be missing outside the publisher's development layout. <br>
Mitigation: Review or replace the local dependency before running npm helper scripts in a new environment. <br>


## Reference(s): <br>
- [Trusted inter-agent messages reference](references/trusted-sessions-send.md) <br>
- [IdentyClaw OpenAPI](https://api.identyclaw.com/openapi.json) <br>
- [OpenClaw issue 57387](https://github.com/openclaw/openclaw/issues/57387) <br>
- [OpenClaw A2A IdentyClaw plugin](https://github.com/discernible-io/openclaw-a2a-idc-plugin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON envelope examples, formatted trusted-message text, and JSON verification results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured IdentyClaw credentials and OpenClaw plugins for live HOLA creation, HOLA verification, and A2A transport.] <br>

## Skill Version(s): <br>
0.2.0 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

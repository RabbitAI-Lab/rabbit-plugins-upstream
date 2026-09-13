## Description:

Detects forged approval claims in agent-payment workflows by verifying Fidacy-signed verdicts against issuer public keys before an agent acts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fidacy](https://clawhub.ai/user/fidacy)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent operators use this skill to check signed Fidacy verdicts received from external agents or services before trusting an approval, safety claim, or payment decision. It helps agents reject unverifiable, tampered, stale, or non-approving verdicts before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on externally installed Fidacy packages.

Mitigation: Verify the selected Fidacy packages before installation and prefer pinned versions or a lockfile.

Risk: The optional native OpenClaw plugin may run with broader agent privileges than the Markdown skill.

Mitigation: Review and approve the native plugin separately before enabling it in an agent runtime.

Risk: A signed verdict can still be unsafe to rely on if it is stale, non-approving, or issued by an untrusted party.

Mitigation: Gate actions on signature validity, issuer trust, decision value, and verdict freshness before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fidacy/skills/fidacy-fraud-detector)
- [Fidacy public JWKS](https://api.fidacy.com/.well-known/jwks.json)
- [Fidacy signup](https://app.fidacy.com/signup)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with JavaScript and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

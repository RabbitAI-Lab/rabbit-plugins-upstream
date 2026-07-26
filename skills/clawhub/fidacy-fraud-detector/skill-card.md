## Description: <br>
Detects forged agent-payment approval claims by guiding agents to verify Fidacy-signed verdicts against issuer public keys before acting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fidacy](https://clawhub.ai/user/fidacy) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agent operators use this skill before acting on external approval, safety, or payment-verdict claims to verify Fidacy-signed JWS verdicts and reject forged, tampered, stale, or untrusted approvals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on Fidacy infrastructure and the @fidacy/verify npm package for verification. <br>
Mitigation: Use it only where Fidacy-signed verdict verification is appropriate, and review dependency and service availability expectations before deployment. <br>
Risk: Issuing signed verdicts requires FIDACY_ENGINE_API_KEY, which is a credential. <br>
Mitigation: Store the API key in a managed secret store, avoid committing it to source control, and scope access to agents that issue signed verdicts. <br>
Risk: A valid signature does not by itself prove that the verdict is fresh or from a trusted issuer. <br>
Mitigation: After signature verification, check the verdict decision, assessed_at freshness, and issuer trust before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fidacy/skills/fidacy-fraud-detector) <br>
- [Fidacy Public JWKS](https://api.fidacy.com/.well-known/jwks.json) <br>
- [Fidacy Signup](https://app.fidacy.com/signup) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JavaScript and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Verification uses a Fidacy verdict JWS; issuing signed verdicts uses FIDACY_ENGINE_API_KEY.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

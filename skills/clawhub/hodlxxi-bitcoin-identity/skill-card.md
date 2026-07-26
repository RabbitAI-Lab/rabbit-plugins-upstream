## Description: <br>
Read-only-by-default integration guide for HODLXXI / UBID Bitcoin-native identity discovery, OAuth2/OIDC metadata, LNURL-Auth boundaries, JWT verification guidance, and explicit operator-approved agent handoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hodlxxi](https://clawhub.ai/user/hodlxxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to understand HODLXXI / UBID as a Bitcoin-native identity provider and safely integrate public discovery, OAuth2/OIDC metadata, LNURL-Auth boundaries, JWT verification, and operator-approved agent handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth registration, token exchange, LNURL-Auth sessions, agent job submission, polling, invoice creation, or Lightning payment could affect identity, credentials, workloads, or funds if performed automatically. <br>
Mitigation: Keep the skill in public-read discovery mode by default and require explicit operator approval for exact endpoints, payloads, scopes, wallet actions, and payment behavior before sensitive actions. <br>
Risk: Incorrect JWT trust decisions could accept invalid identity claims. <br>
Mitigation: Verify issuer, audience, expiration, signature algorithm, key id, and current JWKS before trusting identity tokens. <br>


## Reference(s): <br>
- [HODLXXI Universal Bitcoin Identity Layer](https://github.com/hodlxxi/Universal-Bitcoin-Identity-Layer) <br>
- [ClawHub skill page](https://clawhub.ai/hodlxxi/skills/hodlxxi-bitcoin-identity) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with endpoint lists, security boundaries, and integration checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; sensitive OAuth, LNURL-Auth, agent job, polling, invoice, payment, shell, dependency, and filesystem actions require explicit operator approval.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description:

Authenticate to LNURL-auth (LUD-04) services without a wallet, node, or payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dyegolara](https://clawhub.ai/user/dyegolara)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate to services that provide an LNURL-auth Sign in with Lightning challenge. It decodes the challenge, signs it with a local secp256k1 linking key, and can submit the authentication callback after inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authentication helper can send signed login material over plain HTTP.

Mitigation: Use only LNURL-auth challenges whose decoded service and callback URLs are HTTPS, and inspect the callback with --dry-run --json before submitting.

Risk: Using --single-key links the same authentication key across services.

Mitigation: Avoid --single-key unless cross-service linking is intentional.

Risk: The generated master.key controls future LNURL-auth identities.

Mitigation: Protect the master secret file and do not print, paste, or send it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dyegolara/skills/lnurl-auth)
- [Skill homepage](https://github.com/dyegolara/lnurl-auth-agents)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON helper output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper requires Node.js and may use LNURL_AUTH_KEYFILE for the persistent 32-byte master secret.]

## Skill Version(s):

1.3.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

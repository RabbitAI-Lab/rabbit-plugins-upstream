## Description:

Paradym helps agents operate Paradym through an OOMOL-connected account for reading project data and creating OpenID4VC credential offers or verification requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Paradym projects, templates, issued credentials, issuance sessions, and verification sessions, and to create credential offers or verification requests through the OOMOL CLI after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer an official versioned installer with checksum or signature verification, and avoid the curl-to-bash or Invoke-Expression commands as written.

Risk: Write actions can create Paradym credential offers or verification requests.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running any write action.

Risk: Connector actions depend on OOMOL account authentication, Paradym connection state, and provider scopes.

Mitigation: Run login or connection setup only after an auth or connection failure, and avoid exposing or manually handling raw Paradym API tokens.

## Reference(s):

- [Paradym homepage](https://paradym.id)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-paradym)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions executed through the OOMOL connector return JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

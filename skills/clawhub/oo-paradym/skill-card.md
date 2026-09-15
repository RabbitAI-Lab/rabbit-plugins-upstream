## Description:

Paradym (paradym.id) support for reading, creating, and updating data through the OOMOL Paradym connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect Paradym connector schemas, list projects and credential-related resources, retrieve OpenID4VC sessions, and create credential offers or verification requests through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line installer commands that fetch mutable remote scripts.

Mitigation: Prefer official installation documentation, version-pinned packages, and checksum or signature verification before executing installer code.

Risk: Write actions can create OpenID4VC credential offers or verification requests in Paradym.

Mitigation: Confirm the exact action, payload, project, and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Paradym skill page](https://clawhub.ai/oomol/skills/oo-paradym)
- [Paradym homepage](https://paradym.id)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return JSON data and execution metadata through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

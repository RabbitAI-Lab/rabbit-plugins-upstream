## Description:

Shippo (goshippo.com). Use this skill for Shippo requests that read, create, update, validate, or track shipping-related data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Shippo through the OOMOL-connected oo CLI, including creating and retrieving address or parcel objects, validating addresses, listing saved objects, and checking tracking status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may execute mutable remote installer scripts without an integrity check.

Mitigation: Install only from trusted OOMOL delivery paths; prefer reviewing the installer or using a verified package or checksum before running it.

Risk: Write actions can create Shippo account objects such as addresses and parcels.

Mitigation: Confirm the exact action payload and expected account effect with the user before running any action tagged as write.

Risk: Connector access depends on an OOMOL-connected Shippo account and server-side credential handling.

Mitigation: Use the live connector schema for each action, avoid requesting raw credentials, and retry setup only when authentication or connection errors require it.

## Reference(s):

- [Shippo homepage](https://goshippo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

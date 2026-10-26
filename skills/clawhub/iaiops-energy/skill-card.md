## Description:

Guides agents through read-only utility telecontrol monitoring and diagnostics across IEC 60870-5-104, DNP3, and IEC 61850 MMS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Utility engineers and authorized operators use this skill to guide an agent through read-only substation telemetry checks, event analysis, and data-quality diagnostics. It does not support control actions or relay settings changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Even read-only polling generates traffic on operational telecontrol links.

Mitigation: Connect only to authorized endpoints and check link status before deeper interrogation.

Risk: Credentials could be exposed through configuration or chat.

Mitigation: Keep IAIOPS_MASTER_PASSWORD in a secret manager; do not place secrets in configuration or chat.

Risk: The installed package is external to the supplied skill artifact.

Mitigation: Review the external package separately when runtime code provenance checks are required.

Risk: Older processes sharing an audit trail can report verification errors after this release.

Mitigation: Upgrade all processes sharing IAIOPS_HOME to iaiops 0.29 or newer together.

## Reference(s):

- [iaiops-energy release on ClawHub](https://clawhub.ai/zw008/skills/iaiops-energy)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Configuration instructions]

**Output Format:** [Markdown with inline commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only monitoring guidance; no control commands.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Box CLI skill for working with files, folders, metadata, search, and Box AI in headless environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hbkwong](https://clawhub.ai/user/hbkwong)

### License/Terms of Use:


## Use Case:

Developers and automation engineers use this skill to operate Box from headless environments such as CI, servers, and Railway deployments. It helps agents configure Box CLI credentials, browse and manage files and folders, search content, work with metadata, and call Box AI operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Box CLI can access or modify all Box content allowed by the supplied credentials.

Mitigation: Use a dedicated least-privilege Box app or managed user and avoid broad enterprise-wide scopes.

Risk: Credential files can be exposed if they are stored in the workspace, committed to git, or reused on shared CI systems.

Mitigation: Keep credential files outside the workspace and git, restrict file permissions, and isolate or clean ~/.box on shared CI systems.

Risk: Uncontrolled Box CLI package updates can change behavior in production environments.

Mitigation: Pin or otherwise control the Box CLI package version for production use.

## Reference(s):

- [Box CLI Developer Guide](https://developer.box.com/guides/cli/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Box CLI installation and Box app credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

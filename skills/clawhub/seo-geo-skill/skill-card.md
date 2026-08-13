## Description:

Bootstrap the SEO + GEO skill suite by installing the seogeo binary and writing all 48 SEO/GEO skills into detected agent tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to bootstrap the seogeo binary and install the SEO/GEO skill suite into supported local agent tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run a remote installer.

Mitigation: Review the installer before execution and get explicit user agreement before running installation commands.

Risk: --target all can modify multiple detected agent tool skill directories.

Mitigation: Use --dry-run or install to a single explicit target first, then confirm the expected changes before broader installation.

Risk: Checksum verification may not be strict if checksum metadata is unavailable.

Mitigation: Treat the remote installer as executable third-party code and stop if verification fails or cannot be assessed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-geo-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dry-run, target-specific installation, verification, and credential-check commands.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

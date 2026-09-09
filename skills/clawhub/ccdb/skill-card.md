## Description:

Carbonstop CCDB helps agents search, compare, and match carbon emission factors for materials, energy, transport, packaging, food, product carbon footprint, enterprise carbon accounting, and lifecycle assessment tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carbonstop-official](https://clawhub.ai/user/carbonstop-official)

### License/Terms of Use:

MIT-0

## Use Case:

External sustainability, lifecycle assessment, product carbon footprint, and enterprise carbon accounting practitioners use this skill to guide CCDB CLI setup, authentication, emission factor lookup, detail review, and factor suitability comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs users to install a third-party CLI globally, which can modify the user's Node.js tool environment and inherit that environment's trust boundary.

Mitigation: Use an isolated environment where possible, prefer a pinned reviewed ccdb-cli version, and verify checksums or signatures before installation.

Risk: The skill supports API key authentication and could expose credentials if users paste secrets into chat or command arguments.

Mitigation: Inject API keys through controlled secret or environment configuration and avoid printing, storing, or passing credentials in chat-visible commands.

## Reference(s):

- [ClawHub ccdb Skill Page](https://clawhub.ai/carbonstop-official/skills/ccdb)
- [CCDB CLI Repository](https://github.com/carbonstop/ccdb-cli)
- [CCDB CLI Configuration](https://github.com/carbonstop/ccdb-cli/blob/main/docs/CONFIGURATION.md)
- [CCDB CLI Latest Release](https://github.com/carbonstop/ccdb-cli/releases/latest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands, JSON command examples, links, and concise factor-selection rationale.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CCDB factor links, authentication status guidance, troubleshooting notes, and cautions for restricted values or credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

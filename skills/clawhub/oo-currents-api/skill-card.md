## Description:

Provides agents with schema-first access to Currents API news search, latest-news retrieval, and read-only discovery actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to search and retrieve Currents API news data after their OOMOL account and Currents API connection are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unverified code if run blindly.

Mitigation: Install the oo CLI through a verified, version-pinned, vendor-documented method before using the skill.

Risk: Authentication or Currents API connection setup could be triggered unnecessarily by an agent.

Mitigation: Run authentication or connection setup only after a matching auth or connection error and let the user confirm account setup.

## Reference(s):

- [Currents API homepage](https://currentsapi.services)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands executed through the oo CLI return JSON with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

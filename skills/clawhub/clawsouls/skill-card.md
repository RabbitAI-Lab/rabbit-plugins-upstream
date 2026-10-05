## Description:

Helps agents manage workspace personas, browse and publish Souls, and optionally sync encrypted agent memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomleelive](https://clawhub.ai/user/tomleelive)

### License/Terms of Use:

Apache-2.0

## Use Case:

Agent users and developers use this skill to install, switch, restore, create, validate, and publish workspace personas for supported agents, with optional encrypted memory sync on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persona switching changes persistent agent identity and behavior files.

Mitigation: Confirm workspace changes with the user, review the Soul files, and retain a backup for restoration.

Risk: Installation can execute ClawSouls packages from the npm registry without a fixed version.

Mitigation: Trust the package source and prefer a pinned or locally verified CLI installation.

Risk: Publishing exposes persona files, while sync and swarm send encrypted memory to a configured Git remote.

Mitigation: Review files before publishing and confirm the remote and encryption setup before running sync or swarm.

## Reference(s):

- [ClawHub release](https://clawhub.ai/tomleelive/skills/clawsouls)
- [Hermes Agent adapter](HERMES_ADAPTER.md)
- [ZeroClaw adapter design](ZEROCLAW_ADAPTER.md)
- [Soul-Driven Interaction Design](https://doi.org/10.5281/zenodo.18772585)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide creation or replacement of workspace persona files after user confirmation.]

## Skill Version(s):

0.6.6 (source: SKILL.md frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

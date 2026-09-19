## Description:

Enables agents to inspect OOMOL connector schemas and run IPGeolocation.io lookup, timezone, and astronomy actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query IP geolocation, timezone, and astronomy data through an OOMOL-connected IPGeolocation.io account while relying on live action schemas before requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes unverified remote installer scripts for the oo CLI.

Mitigation: Install only through a trusted OOMOL CLI distribution path, or replace the remote installer with a pinned and verified manual installation process; avoid agent-run installation from elevated shells.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ipgeolocation-io)
- [IPGeolocation.io homepage](https://ipgeolocation.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on live IPGeolocation.io connector schemas and the user's OOMOL account connection state.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

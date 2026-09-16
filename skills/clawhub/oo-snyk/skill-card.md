## Description:

Operate Snyk through an OOMOL-connected account to search and read organizations, projects, issues, and authenticated principal data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to query Snyk data through OOMOL's connected account flow, including organizations, projects, issues, and the authenticated principal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes internet-downloaded installer scripts for the oo CLI.

Mitigation: Install the oo CLI only through a verified package or documented process after inspecting the source and approving the exact command.

Risk: Snyk data is accessed through an OOMOL-connected account with server-side credential injection.

Mitigation: Confirm that routing Snyk reads through OOMOL is acceptable for the organization's security data before use.

## Reference(s):

- [ClawHub Snyk skill](https://clawhub.ai/oomol/skills/oo-snyk)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Snyk homepage](https://snyk.io)
- [Snyk skill icon](https://static.oomol.com/logo/third-party/snyk.svg)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused Snyk connector actions return structured JSON with execution metadata; setup requires the oo CLI, OOMOL authentication, and a connected Snyk account.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

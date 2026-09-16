## Description:

Operates Supervisely through an OOMOL-connected account to read user, team, workspace, project, and dataset data with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Supervisely account resources through OOMOL's connected oo CLI workflow without handling raw Supervisely credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to pipe remote installer scripts directly into a shell.

Mitigation: Install the oo CLI only from a trusted source; prefer a verified or package-managed install path and review installer contents before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-supervisely)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Supervisely](https://supervisely.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON data]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supervisely connector results are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

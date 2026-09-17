## Description:

Rootly (rootly.com) integration that lets agents search and read Rootly data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Rootly schemas and retrieve the current user, incidents, services, and teams through an OOMOL-connected Rootly account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run remote installer scripts directly in a shell.

Mitigation: Review the installer source and prefer a pinned, verified oo CLI installation method before installing.

Risk: Future Rootly connector actions could write, remove, or overwrite Rootly data if added later.

Mitigation: Require the agent to inspect the live schema and confirm the exact payload and effect with the user before any write or destructive action.

## Reference(s):

- [Rootly homepage](https://rootly.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to fetch live action schemas before running Rootly connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

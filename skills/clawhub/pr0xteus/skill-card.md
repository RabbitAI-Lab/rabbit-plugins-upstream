## Description:

pr0xteus guides agents in allocating, inspecting, and safely using trusted WireGuard-backed SOCKS5 and HTTP exits through a private bearer-protected controller.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up or talk to a trusted pr0xteus controller, allocate approved country or pool egress, inspect active leases and cells, and replace failed assignments without exposing an open proxy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Controller tokens and returned proxy URLs can grant access to private egress.

Mitigation: Protect PR0XTEUS_API_TOKEN and proxy URLs as credentials, and keep them out of logs, issue trackers, and public services.

Risk: Allocating exits or deleting cells can consume provider capacity or disrupt active egress.

Mitigation: Only allocate country or pool exits and delete cells when the user explicitly intends that action.

Risk: Installer and Docker setup affect local configuration, containers, and WireGuard-backed routing.

Mitigation: Review the downloaded installer before running it and install only for a pr0xteus controller you operate and trust.

## Reference(s):

- [pr0xteus setup](artifact/references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pr0xteus)
- [Project homepage](https://github.com/psyb0t/pr0xteus)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, and YAML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a trusted pr0xteus controller and user-provided PR0XTEUS_URL and PR0XTEUS_API_TOKEN; no MCP tools are provided.]

## Skill Version(s):

0.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

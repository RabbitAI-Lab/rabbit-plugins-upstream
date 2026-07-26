## Description: <br>
Manage multiple paths with Tailscale Serve, serving files, directories, or ports simultaneously without conflicts and control via background mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[snopoke](https://clawhub.ai/user/snopoke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage Tailscale Serve routes for local files, directories, and services, including checking current routes, adding non-conflicting paths, and resetting or removing routes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tailscale Serve routes can expose user-selected local files, folders, or services to a Tailscale network. <br>
Mitigation: Check `tailscale serve status` before running examples, serve only narrow non-sensitive paths or ports, and avoid broad personal directories or unauthenticated admin and development endpoints. <br>
Risk: Background serve routes can remain active after configuration commands are run. <br>
Mitigation: Verify active routes after changes and turn off specific paths or run `tailscale serve reset` when routes are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/snopoke/skills/tailscale-serve) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

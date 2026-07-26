## Description: <br>
Aria2 Downloader helps an agent submit and manage aria2 downloads for magnet links, torrent files, and HTTP URLs, with a documented handoff to a host-side 115 cloud transfer workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ahiven](https://clawhub.ai/user/ahiven) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent submit magnet, torrent, or HTTP downloads to an aria2 RPC service and check, pause, resume, or remove tasks. It is intended for environments where aria2 and any optional completion hook are already configured by the host. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports a fixed aria2 RPC token in the skill examples. <br>
Mitigation: Replace the token with a unique secret or environment variable before use, and keep aria2 RPC access protected. <br>
Risk: The documented completion workflow can transfer completed files to 115 cloud storage and remove local files. <br>
Mitigation: Inspect the host-side completion script before enabling it, restrict it to a dedicated download directory, and explicitly accept local deletion behavior. <br>
Risk: An exposed aria2 RPC service could allow unauthorized download control. <br>
Mitigation: Keep the RPC service bound to localhost or otherwise protected before using the generated commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ahiven/skills/aria2) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an existing aria2 RPC service and a user-supplied RPC secret.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Control Sonos speakers (discover/status/play/volume/group). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to have an agent help discover local Sonos speakers, check status, control playback and volume, manage groups, favorites, queues, and optional Spotify search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can change playback, volume, grouping, party mode, and queue contents on shared Sonos networks. <br>
Mitigation: Review proposed Sonos commands before execution and confirm the target speaker or group, especially when using volume, grouping, party mode, or queue operations. <br>
Risk: Optional Spotify search requires Spotify credentials. <br>
Mitigation: Configure Spotify credentials only when Spotify search is needed and handle them as secrets. <br>
Risk: The Go install target uses the latest upstream module version. <br>
Mitigation: Pin or review the Go module when reproducible installs or stricter supply-chain review is required. <br>


## Reference(s): <br>
- [Sonos CLI homepage](https://sonoscli.sh) <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/sonoscli) <br>
- [Publisher profile](https://clawhub.ai/user/steipete) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target Sonos devices on the local network; Spotify search needs optional Spotify credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

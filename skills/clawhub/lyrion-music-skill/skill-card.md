## Description: <br>
Controls Lyrion Music Server over its JSON-RPC API for playback, volume, playlist, player selection, and music library queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[photonixlaser-ux](https://clawhub.ai/user/photonixlaser-ux) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users can use this skill to control a Lyrion Music Server on a trusted network, including playback, volume, playlists, player power, and music database search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real changes to a music system, including playback, volume, power, playlist add, and playlist clear actions. <br>
Mitigation: Install it only when agent control of the LMS instance is intended, and review commands before execution. <br>
Risk: The skill sends network commands to a configured Lyrion Music Server endpoint. <br>
Mitigation: Set LYRION_HOST and LYRION_PORT explicitly and use the skill only on a trusted network. <br>


## Reference(s): <br>
- [Lyrion Music Server API Reference](references/api.md) <br>
- [Official Lyrion CLI Reference](https://lyrion.org/reference/cli/) <br>
- [LMS Community slimserver GitHub](https://github.com/LMS-Community/slimserver) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses LYRION_HOST and LYRION_PORT to target the Lyrion Music Server JSON-RPC endpoint.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

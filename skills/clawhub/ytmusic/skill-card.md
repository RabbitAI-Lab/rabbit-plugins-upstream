## Description: <br>
Manage YouTube Music library, playlists, and discovery via ytmusicapi. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gentrycopsy](https://clawhub.ai/user/gentrycopsy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to help an agent manage a YouTube Music account, including library items, playlists, lyrics, and discovery workflows through ytmusicapi. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires local authentication files that should be treated as account secrets. <br>
Mitigation: Keep browser.json private, delete headers.txt after setup, and do not commit either file to source control. <br>
Risk: Library and playlist actions can modify the user's YouTube Music account. <br>
Mitigation: Ask the agent to confirm before making library or playlist changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gentrycopsy/skills/ytmusic) <br>
- [YouTube Music](https://music.youtube.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent actions depend on local ytmusicapi authentication files and may change the user's YouTube Music library or playlists.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

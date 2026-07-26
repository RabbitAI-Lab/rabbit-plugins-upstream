## Description: <br>
Trakt helps agents query Trakt.tv watch history and search for movies or TV shows through a local Trakt CLI setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to answer questions about recent watched movies and TV shows, retrieve Trakt watch history, and search Trakt titles through the local trakt-cli setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on the npm trakt-cli package and locally stored Trakt app credentials. <br>
Mitigation: Install only if you trust trakt-cli, review the Trakt authorization during setup, keep ~/.trakt.yaml private, and revoke the app token from Trakt if you stop using the skill. <br>
Risk: Watch history responses may expose personal viewing activity. <br>
Mitigation: Use the skill's read-only Trakt workflow and avoid sharing command output containing private watch history unless intended. <br>


## Reference(s): <br>
- [Trakt](https://trakt.tv) <br>
- [Trakt OAuth Applications](https://trakt.tv/oauth/applications/new) <br>
- [ClawHub Skill Page](https://clawhub.ai/mjrussell/skills/trakt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search works without authentication; watch history requires Trakt authentication and local credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Tracks and recommends TV shows and movies through Trakt.tv, including watch history, watchlists, search, trending content, and personalized suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fr3nch13](https://clawhub.ai/user/fr3nch13) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent developers use this skill to connect an OpenClaw assistant to a Trakt.tv account for watch recommendations, watch history summaries, watchlist checks, search, and trending entertainment queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores Trakt client credentials and tokens in ~/.openclaw/trakt_config.json. <br>
Mitigation: Protect the configuration file with owner-only permissions and avoid sharing credentials or tokens in chat, logs, or support transcripts. <br>
Risk: The skill can maintain ongoing access to Trakt viewing data after authentication. <br>
Mitigation: Use the narrowest Trakt application permissions that support the desired workflow and revoke access from Trakt if the skill is no longer needed. <br>
Risk: State-changing commands can modify Trakt watch history. <br>
Mitigation: Require explicit user confirmation before commands that mark content watched or otherwise change account data. <br>
Risk: The setup flow may install Python dependencies into the system environment. <br>
Mitigation: Prefer a virtual environment for dependency installation before running the setup or client scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fr3nch13/skills/openclaw-trakt) <br>
- [Trakt API documentation](https://trakt.docs.apiary.io/) <br>
- [Trakt application settings](https://trakt.tv/oauth/applications) <br>
- [Trakt API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read Trakt viewing data and update watch history through authenticated API calls.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

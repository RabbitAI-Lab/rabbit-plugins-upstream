## Description: <br>
Provides detailed music data and user information from Last.fm, including artists, albums, tracks, charts, tags, and user listening statistics via the Last.fm API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[keyfrog-21k](https://clawhub.ai/user/keyfrog-21k) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to construct Last.fm API requests for music metadata, charts, tags, and user listening statistics. It is most useful when an agent needs concise guidance for querying Last.fm resources with an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Last.fm user endpoints may expose personal listening patterns. <br>
Mitigation: Use user endpoints only for user-directed queries and avoid unnecessary storage or sharing of retrieved profile or listening data. <br>
Risk: Request examples require a Last.fm API key, which can be exposed if copied into shared logs or committed files. <br>
Mitigation: Keep API keys in local secrets or environment variables and avoid sharing request URLs that contain real keys. <br>


## Reference(s): <br>
- [Last.fm API](https://www.last.fm/api) <br>
- [ClawHub skill page](https://clawhub.ai/keyfrog-21k/skills/last-fm) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown with HTTP request examples and parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Last.fm API key for live API requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

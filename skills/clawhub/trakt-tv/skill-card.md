## Description: <br>
Interact with the Trakt API to manage your watchlist, collection, ratings, and discover content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[d-meagher](https://clawhub.ai/user/d-meagher) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent query and update a Trakt.tv account, including watchlists, viewing history, collections, ratings, search, trending content, and recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent read or change a user's Trakt account. <br>
Mitigation: Install only when account access is intended, and ask for confirmation before removals, ratings, watch-history changes, or bulk updates. <br>
Risk: Trakt client secrets, access tokens, and refresh tokens may be exposed through shared terminal output or committed configuration. <br>
Mitigation: Keep tokens private, restrict local config access, avoid sharing command output containing credentials, and rotate or revoke exposed tokens. <br>
Risk: Authenticated Trakt API requests can modify watchlists, collections, ratings, and history. <br>
Mitigation: Review generated curl commands and JSON payloads before execution, especially for write, remove, or batch operations. <br>


## Reference(s): <br>
- [Trakt.tv](https://trakt.tv) <br>
- [Trakt API Documentation](https://trakt.docs.apiary.io/) <br>
- [Trakt Applications](https://trakt.tv/oauth/applications) <br>
- [AgentSkills Specification](https://agentskills.io/) <br>
- [ClawHub Skill Page](https://clawhub.ai/d-meagher/skills/trakt-tv) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Trakt OAuth credentials supplied through environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

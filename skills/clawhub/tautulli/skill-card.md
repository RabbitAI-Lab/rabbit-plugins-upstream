## Description: <br>
Monitor Plex activity and stats via the Tautulli API, including current streams, watch history, library stats, recently added media, users, and server info. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rjmurillo](https://clawhub.ai/user/rjmurillo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an OpenClaw agent query a configured Tautulli instance for Plex activity, library, user, and server status information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive Plex viewing activity, watch history, usernames, and server metadata. <br>
Mitigation: Install it only where that activity data is appropriate for the agent to read, and limit access to trusted workspaces. <br>
Risk: TAUTULLI_API_KEY grants access to the configured Tautulli API and could be exposed through logs, screenshots, shell history, or repositories. <br>
Mitigation: Store the key in environment configuration, avoid sharing it in prompts or logs, prefer HTTPS for TAUTULLI_URL, and rotate the key if exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rjmurillo/skills/tautulli) <br>
- [Tautulli](https://tautulli.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text and Markdown with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, TAUTULLI_URL, and TAUTULLI_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

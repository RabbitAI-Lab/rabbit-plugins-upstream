## Description: <br>
Streaming Buddy helps agents track viewing activity, learn entertainment preferences, and recommend movies or TV shows by service, mood, and availability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[udiedrichsen](https://clawhub.ai/user/udiedrichsen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to search streaming content, manage viewing history and watchlists, and request personalized movie or TV recommendations based on services, mood, ratings, and learned preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Streaming services, watch history, ratings, inferred preferences, cached TMDB responses, and the TMDB API key are stored in the workspace. <br>
Mitigation: Use a TMDB key intended for this skill, avoid storing sensitive viewing data in shared workspaces, and delete $WORKSPACE/memory/streaming-buddy/ to reset the local profile. <br>
Risk: Search terms and TMDB requests are sent to TMDB when the skill searches, fetches details, or builds recommendations. <br>
Mitigation: Use the skill only for search terms appropriate to send to TMDB, and review configured region and language before use. <br>
Risk: Streaming availability can be delayed or region-dependent, so recommendations may not match a user's current subscriptions. <br>
Mitigation: Confirm availability in the user's streaming service before acting on a recommendation, especially for new releases or regional catalogs. <br>


## Reference(s): <br>
- [Streaming Buddy release page](https://clawhub.ai/udiedrichsen/skills/streaming-buddy) <br>
- [Streaming Services Reference](references/services.md) <br>
- [TMDB API Reference](references/tmdb-api.md) <br>
- [JustWatch Integration](references/justwatch.md) <br>
- [TMDB API key setup](https://www.themoviedb.org/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON command responses and concise agent-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq, curl, and a TMDB API key; stores profile, preferences, services, watchlist, history, and cached API responses under the workspace memory directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

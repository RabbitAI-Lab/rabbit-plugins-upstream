## Description: <br>
Request movies or TV shows on Overseerr by title and optional season, checking availability before forwarding the request to Sonarr or Radarr. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trialskid](https://clawhub.ai/user/trialskid) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and media server operators use this skill to ask an agent to search their Overseerr instance and submit movie or TV requests, including specific TV seasons, after checking for existing availability or prior requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit requests to a user's Overseerr instance using an API key. <br>
Mitigation: Store the API key securely and use the least-privileged key available. <br>
Risk: Ambiguous title matches could result in requesting the wrong movie or TV show. <br>
Mitigation: Review ambiguous title matches and require user clarification before creating the request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/trialskid/skills/overseerr-request-media) <br>
- [Publisher profile](https://clawhub.ai/user/trialskid) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and short confirmation text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the user's OVERSEERR_URL and OVERSEERR_API_KEY to search, disambiguate, check status, and submit media requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Provides Fantasy NBA Israel league statistics, rankings, team details, player rosters, and shooting analysis through the XiaoBenYang-backed API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Fantasy NBA league participants and agents use this skill to retrieve team lists, rotisserie rankings, actual per-game averages, team details, player rosters, and shooting statistics for the Israel league. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release was flagged suspicious because of mismatched documentation and under-disclosed API-key persistence. <br>
Mitigation: Review the skill before installation, confirm the Fantasy NBA purpose, and clean up unrelated gaokao or school-query references before using it in a sensitive environment. <br>
Risk: The skill requires an API key for the XiaoBenYang-backed service and stores it in a local .env file. <br>
Mitigation: Provide credentials only if you trust the service, keep .env out of version control, and remove the key when it is no longer needed. <br>
Risk: The release guidance calls out dependency pinning or updates before trusting the skill in sensitive environments. <br>
Mitigation: Pin or update dependencies in a controlled environment before relying on the skill for production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/fantasynbaleague) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration guidance] <br>
**Output Format:** [Markdown summaries of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY credential; API responses may include raw league, team, player, ranking, and shooting-stat data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

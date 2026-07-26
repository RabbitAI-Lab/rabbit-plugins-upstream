## Description: <br>
Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and contributors use this skill to plan fair GitLab hackathon participation, verify event requirements, select qualifying issues and merge requests, and keep contributions reviewable and rule-compliant. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated GitLab commands or recommendations may affect public issues, merge requests, labels, closures, or comments. <br>
Mitigation: Use a GitLab token with the minimum required scope and review every glab command before execution. <br>
Risk: Hackathon rules, dates, scoring, and prize requirements may change between runs. <br>
Mitigation: Verify the current GitLab hackathon pages and API before optimizing work or submitting entries. <br>


## Reference(s): <br>
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon) <br>
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current) <br>
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon) <br>
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference glab, jq, curl, and a GitLab token configured with the minimum required scope.] <br>

## Skill Version(s): <br>
1.75.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

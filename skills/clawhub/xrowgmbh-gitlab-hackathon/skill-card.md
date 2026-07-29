## Description: <br>
Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external contributors use this skill to plan fair GitLab hackathon participation, choose qualifying issues or merge requests, and track scoring requirements without abusing comments, labels, closures, or commit volume. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to use GitLab tooling with a GitLab token to inspect issues or merge requests and perform contribution workflow actions. <br>
Mitigation: Use a properly scoped token and review proposed labels, comments, issue closures, and merge requests before submission. <br>
Risk: Hackathon score optimization can encourage spam comments, padded commits, incorrect labels, or invalid issue closures if the guidance is misused. <br>
Mitigation: Apply only legitimate workflow actions, link merge requests to real issues, wait for passing checks before review requests, and follow the current GitLab hackathon rules. <br>


## Reference(s): <br>
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon) <br>
- [GitLab Current Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current) <br>
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon) <br>
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and checklist-style guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference glab, jq, curl, and GITLAB_TOKEN when GitLab operations are needed.] <br>

## Skill Version(s): <br>
1.77.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

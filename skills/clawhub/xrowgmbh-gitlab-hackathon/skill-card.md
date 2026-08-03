## Description: <br>
Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and GitLab contributors use this skill to plan fair hackathon participation, select reviewable issues and merge requests, verify live rules and scoring, and avoid rule-abuse patterns while working toward qualifying submissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitLab token and API access could allow broader repository actions than the user intends. <br>
Mitigation: Use a least-privilege GitLab token where possible and review proposed glab or API commands before execution. <br>
Risk: Hackathon rules, dates, scoring, or prize requirements may change after the skill text was authored. <br>
Mitigation: Verify the live GitLab hackathon pages and current API before selecting work or optimizing for scoring. <br>
Risk: Score-focused activity could drift into spam comments, padded commits, incorrect labels, invalid closures, or other unfair behavior. <br>
Mitigation: Follow the skill's fair-use guidance: prioritize real reviewable contributions, link only relevant issues, avoid exploit-like behavior, and ask maintainers for clarification when needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-hackathon) <br>
- [GitLab Quarterly Hackathon](https://contributors.gitlab.com/hackathon) <br>
- [Current GitLab Hackathon API](https://contributors.gitlab.com/api/v1/hackathons/current) <br>
- [GitLab Transcend Hackathon](https://contributors.gitlab.com/transcend-hackathon) <br>
- [GitLab Contribution Points](https://contributors.gitlab.com/docs/user-guide#contribution-points) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline bash commands and checklist items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose GitLab CLI and API commands that require glab, jq, curl, and GITLAB_TOKEN.] <br>

## Skill Version(s): <br>
1.78.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Automates X posting by using browser control to scrape trends, generate tweet ideas, queue approvals, and publish through a logged-in X account without X API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nightfullstar](https://clawhub.ai/user/nightfullstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and teams use this skill to generate, approve, schedule, and publish X posts from trend data through a local browser session. It is intended for users who are comfortable letting agent automation operate a logged-in social media account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a logged-in X account and publish posts with weak safeguards. <br>
Mitigation: Use a dedicated browser profile or test account, keep per-post approval enabled, and review queued posts before publishing. <br>
Risk: Cron or full-auto usage could post more often or more broadly than intended. <br>
Mitigation: Avoid unattended full-auto mode unless strict daily limits, scheduling boundaries, and a manual kill switch are in place. <br>
Risk: Local trend, queue, and history files may contain account activity or draft content. <br>
Mitigation: Review and clear local data files as needed, and avoid sharing runtime data with published skill artifacts. <br>
Risk: The skill's credential-free and Terms-of-Service claims are not security or compliance guarantees. <br>
Mitigation: Review X platform rules and organizational policy before using browser automation on a real account. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nightfullstar/skills/x-automation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and local JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local trend, approval queue, and tweet history JSON files under data/.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

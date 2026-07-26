## Description: <br>
Automates the process of identifying trends on X (Twitter), generating opinionated/engaging content, and posting it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[harshhmaniya](https://clawhub.ai/user/harshhmaniya) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and content operators use this skill to identify X trends, draft candidate posts, select a high-engagement option, and publish it through a logged-in X account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish public X posts from a logged-in account without a final approval step. <br>
Mitigation: Require manual approval of the exact post text and destination account before publishing. <br>
Risk: The skill uses the user's logged-in X session to read content and publish posts. <br>
Mitigation: Use a dedicated browser profile or test account when possible, and confirm the active account before posting. <br>
Risk: Candidate posts and errors are written to memory logs. <br>
Mitigation: Periodically review or clear the memory logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/harshhmaniya/skills/x-post-automation) <br>
- [Publisher profile](https://clawhub.ai/user/harshhmaniya) <br>
- [X Home](https://x.com/home) <br>
- [X Explore](https://x.com/explore/) <br>
- [X Compose](https://x.com/compose/post) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Files, Guidance] <br>
**Output Format:** [Markdown and browser actions with logged text drafts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces candidate posts, publishes selected content through a logged-in X session, and logs candidates or failures for review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

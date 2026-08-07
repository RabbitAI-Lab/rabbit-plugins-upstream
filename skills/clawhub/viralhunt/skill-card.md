## Description: <br>
Discover what's trending or going viral across TikTok, Instagram, X, Facebook, Pinterest, and Reddit, and schedule or publish posts to the user's connected social accounts through the ViralHunt.io API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rodvan](https://clawhub.ai/user/rodvan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and social media operators use this skill to research trending content, curate post ideas, and manage publishing or scheduling across their own connected social accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish, schedule, edit, or cancel posts on real connected social accounts. <br>
Mitigation: Require the agent to show the exact project, target accounts, content, media, and posting time, then wait for explicit user approval before taking any publishing, scheduling, editing, or cancellation action. <br>
Risk: The ViralHunt API token can enable actions on connected accounts through the ViralHunt service. <br>
Mitigation: Install and use the skill only when the ViralHunt service is trusted, keep the token scoped to the intended account, and ask for a fresh token if the API reports that the token is missing or revoked. <br>
Risk: Reposting inaccurate, copyrighted, or spam-like content can harm connected social accounts. <br>
Mitigation: Review proposed posts for accuracy, permissions, and platform policy fit before approving publication or scheduling. <br>


## Reference(s): <br>
- [ViralHunt](https://viralhunt.io) <br>
- [ViralHunt API Documentation](https://viralhunt.io/api) <br>
- [ClawHub Skill Page](https://clawhub.ai/rodvan/skills/viralhunt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API Calls, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with JSON payload examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute API requests that read trends, upload media, schedule posts, publish immediately, edit scheduled posts, cancel scheduled posts, or check posting status.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

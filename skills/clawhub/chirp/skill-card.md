## Description: <br>
X/Twitter CLI using OpenClaw browser tool for reading timelines, posting tweets, liking, retweeting, replying, searching, and related browser-based account actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zizi-cat](https://clawhub.ai/user/zizi-cat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to guide an agent operating a logged-in X/Twitter browser session for timeline reading, posting, engagement, profile viewing, and search. The user should confirm account, target, and content before public account actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide public actions from a logged-in X/Twitter account, including posting, replying, reposting, liking, and following. <br>
Mitigation: Confirm the exact account, target, and content before any public account action. <br>
Risk: Use of an existing browser session can expose the user's normal account context to agent-operated actions. <br>
Mitigation: Use a separate browser profile or test account when limiting account exposure is important. <br>
Risk: Browser UI references change between snapshots and may point to stale controls. <br>
Mitigation: Take a fresh browser snapshot before each action and use the current control reference. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance] <br>
**Output Format:** [Markdown with browser command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an OpenClaw browser profile with an authenticated X/Twitter session.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

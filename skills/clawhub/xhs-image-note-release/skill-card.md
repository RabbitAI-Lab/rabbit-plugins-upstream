## Description: <br>
Automates Xiaohongshu image-note publishing with ego-browser, including image upload, title and body entry, hashtag handling, and publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and content operators use this skill to prepare and publish image-based Xiaohongshu posts from an agent workflow. It is intended for accounts already logged in through ego-lite and configured with the required image, title, and body inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish directly to a live Xiaohongshu account without a final confirmation step. <br>
Mitigation: Review the selected account, title, body, image list, visibility settings, and platform limits before running it; prefer adding a dry-run or explicit confirmation step before publication. <br>
Risk: The skill uses the logged-in Xiaohongshu browser session available to ego-browser. <br>
Mitigation: Run it only in a browser profile logged into the intended account and verify the account state before publishing. <br>
Risk: Repeated automated publishing may trigger platform rate limits or moderation controls. <br>
Mitigation: Space out runs and manually review platform feedback after each post. <br>


## Reference(s): <br>
- [Publish method reference](references/publish-method.md) <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/xhs-image-note-release) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/songhonglei) <br>
- [Xiaohongshu creator publish page](https://creator.xiaohongshu.com/publish/publish) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires IMAGE_DIR, IMAGES, TITLE, and BODY environment-style inputs plus an active ego-browser session.] <br>

## Skill Version(s): <br>
1.2.2 (source: frontmatter, changelog, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

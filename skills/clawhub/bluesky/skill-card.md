## Description: <br>
Use the Bluesky CLI for timeline, search, notifications, posts, replies, threads, images, likes, reposts, follows, blocks, and mutes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate a Bluesky account through a local CLI for reading timelines, search results, notifications, and threads, and for preparing or executing posts, replies, engagement, social graph, and moderation actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post publicly and change Bluesky account state, including delete, follow, block, mute, and repost actions. <br>
Mitigation: Use dry-run for public posts when final text is not already approved, verify exact account or post targets before mutations, and set BSKY_CONFIRM_MUTATIONS=1 for confirmation prompts. <br>
Risk: Bluesky app passwords or local sessions could be exposed or misused if handled carelessly. <br>
Mitigation: Use the hidden app-password prompt, do not paste app passwords into chat or command arguments, revoke app passwords from Bluesky settings when needed, and rely on owner-only local session file permissions. <br>


## Reference(s): <br>
- [ClawHub Bluesky skill page](https://clawhub.ai/jeffaf/skills/bluesky) <br>
- [Bluesky](https://bsky.app) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON output from read commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide local CLI setup, propose Bluesky commands, and use dry-run or JSON flags where supported.] <br>

## Skill Version(s): <br>
1.6.3 (source: SKILL.md frontmatter and changelog, released 2026-06-05) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Publish content to Mastodon when you need to post a Mastodon status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[behrangsa](https://clawhub.ai/user/behrangsa) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to publish one or more Mastodon statuses, optionally with visibility, language, scheduling, quote approval, and media attachment settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish real Mastodon posts using the user's account token. <br>
Mitigation: Confirm the target account, post text, visibility, schedule, and media before each run; use a revocable token with only the permissions needed to post. <br>
Risk: Media attachment paths can disclose or upload unintended local files. <br>
Mitigation: Review every media file path before execution and avoid attaching sensitive or private files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/behrangsa/skills/tootbot) <br>
- [Clawdbot](https://github.com/anthropics/clawdbot) <br>
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills) <br>
- [ClawdHub tootbot page](https://clawdhub.com/skills/tootbot) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON status input] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Bun plus MASTODON_URL and MASTODON_ACCESS_TOKEN; supports one or more statuses with optional visibility, language, scheduling, quote policy, and media attachments.] <br>

## Skill Version(s): <br>
0.5.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

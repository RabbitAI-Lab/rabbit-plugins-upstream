## Description: <br>
Uploads a local video to Douyin Creator Center through a logged-in Chrome session, fills the description, sets visibility, and optionally publishes it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juzanxie-dev](https://clawhub.ai/user/juzanxie-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill to have an agent upload a local video into an existing Douyin Creator Center browser session, set the description and visibility, and either publish or stop for manual review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill controls a logged-in Douyin Creator Center browser tab and can publish content through that session. <br>
Mitigation: Review the target file path, title, visibility, --publish setting, and CDP endpoint before each run; use --publish false to upload and inspect before posting. <br>
Risk: Publishing may trigger SMS verification or other account checks that the automation cannot complete. <br>
Mitigation: Handle verification manually in the browser session; the skill does not request or fill SMS verification codes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juzanxie-dev/skills/douyin-creator-upload) <br>
- [Publisher profile](https://clawhub.ai/user/juzanxie-dev) <br>
- [Douyin Creator Center upload page](https://creator.douyin.com/creator-micro/content/upload) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and argument guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill emits step logs and exit codes while driving browser automation through Chrome DevTools Protocol.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, frontmatter, package.json, CHANGELOG released 2026-07-07) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
PT Agent helps authorized users search private trackers, review account and downloader status, configure supported tracker connections, and hand selected results to a downloader. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xzulab](https://clawhub.ai/user/xzulab) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to operate authorized private-tracker accounts through natural-language search, account status checks, downloader queue review, and selected-result download handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control configured private trackers and downloader operations, including immediate-start downloads and resume-all behavior. <br>
Mitigation: Install only for users who intentionally want this control, and review or disable public-site presets, generic magnet adding, immediate-start downloads, and resume-all behavior when stricter confirmation is required. <br>
Risk: Private tracker credentials, passkeys, cookies, tokens, private download URLs, and torrent data can expose account access or personal activity if pasted into chat, logs, or configuration files. <br>
Mitigation: Use credential references such as env://, secret://, profile://, or proxy:// and rotate any secret that was exposed in a shared or public environment. <br>
Risk: The security verdict is suspicious because the skill includes broader downloader-control and public-torrent surfaces. <br>
Mitigation: Review the security guidance before installation and restrict the enabled adapters and downloader actions to the user's authorized scope. <br>


## Reference(s): <br>
- [PT Agent on ClawHub](https://clawhub.ai/xzulab/skills/pt-agent) <br>
- [PT-depiler](https://github.com/pt-plugins/PT-depiler) <br>
- [First Run Guide](references/first-run-guide.md) <br>
- [Runtime Policy](references/runtime-policy.md) <br>
- [Downloader Integration](references/downloader-integration.md) <br>
- [Agent Contract](references/agent-contract.md) <br>
- [Adapter Catalog](references/adapter-catalog.json) <br>
- [Site Preset Catalog](references/site-preset-catalog.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Concise natural-language responses with numbered result lists, status summaries, and configuration prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute bundled Python runtime commands for authorized tracker and downloader operations; user-facing responses should not expose secrets, raw private URLs, local paths, or backend mechanics.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

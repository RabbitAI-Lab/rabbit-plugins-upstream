## Description: <br>
Schedules and posts text, media, threads, and bulk content across Discord, Reddit, Twitter/X, Mastodon, Bluesky, Moltbook, LinkedIn, and Telegram. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrshorrid](https://clawhub.ai/user/mrshorrid) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and agent builders use this skill to schedule, queue, publish, and monitor social posts across multiple platforms from an OpenClaw-compatible Node.js toolset. It supports immediate posts, daemon-based scheduling, bulk calendars, threads, media upload workflows, and a local dashboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post publicly from connected social media accounts and uses powerful platform credentials. <br>
Mitigation: Use test or least-privilege accounts first, review every queued post before daemon execution, and avoid automatic posting of sensitive or unapproved content. <br>
Risk: Credential configuration, queue storage, and dashboard access may expose posting authority if handled carelessly. <br>
Mitigation: Protect credential files and storage/queue.json, avoid command-line secrets where possible, restrict dashboard access, and disable the dashboard when it is not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mrshorrid/skills/social-scheduler) <br>
- [Artifact README](artifact/README.md) <br>
- [Media guide](artifact/MEDIA-GUIDE.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Files] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, Node.js CLI commands, queue files, and platform API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local queue, analytics, credential configuration, and media-related files when the user runs the included scripts.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

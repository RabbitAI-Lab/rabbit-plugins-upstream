## Description: <br>
Schedule and post text, media, and threads to Discord, Reddit, Twitter/X, Mastodon, Bluesky, and Moltbook via API with immediate or scheduled publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrshorrid](https://clawhub.ai/user/mrshorrid) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to prepare, publish, schedule, queue, and cancel social posts across supported platforms. It is useful when an agent needs CLI-driven social publishing with JSON credential files and platform-specific setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish content to real social accounts when supplied with valid platform credentials. <br>
Mitigation: Use test accounts first, review scheduled content before daemon execution, and grant only the minimum platform permissions needed. <br>
Risk: Credential files, webhook URLs, API keys, and queue data may expose account access if stored or shared carelessly. <br>
Mitigation: Keep credentials and queues outside version control with restricted file permissions, and avoid passing live secrets directly on the command line. <br>
Risk: Untrusted prompts could choose local media paths or remote media URLs that should not be posted or fetched. <br>
Mitigation: Constrain allowed paths and domains, review media inputs before execution, and block untrusted prompts from controlling file paths or URLs. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/mrshorrid/skills/openclaw-social-scheduler) <br>
- [SKILL.md usage guide](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [Media upload guide](artifact/MEDIA-GUIDE.md) <br>
- [Moltbook usage guide](artifact/MOLTBOOK-USAGE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, JSON configuration examples, and console or JSON command output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces social publishing actions through platform APIs when the generated commands are executed with valid credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence; artifact/package.json declares 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
AI WeChat Feed scans AI WeChat public account articles, ranks high-read content, clusters topics, and generates a styled HTML daily report with search and optional subscription support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External AI professionals, content creators, content operations teams, and industry researchers use this skill to generate daily AI WeChat content briefings, filter by topics, and monitor article trends over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The --subscribe option creates persistent, credential-backed local scheduling behavior. <br>
Mitigation: Review the subscription behavior before enabling it, use --unsubscribe when no longer needed, and inspect local LaunchAgent or crontab entries if the scheduled job must be removed manually. <br>
Risk: The skill can use a RedFox API key from an environment variable, command line argument, or plaintext local config file. <br>
Mitigation: Prefer REDFOX_API_KEY or a short-lived key over a plaintext config file, avoid exposing the key in prompts or logs, and rotate or revoke the key when removing the skill. <br>
Risk: Generated reports may contain fetched third-party content and browser JavaScript for search. <br>
Mitigation: Keep generated reports private, review report content before sharing, and only open reports from trusted local runs. <br>
Risk: Interactive search depends on a local browser-accessible proxy while the report service is running. <br>
Mitigation: Run the local search service only when needed, close the terminal session to stop it, or use --no-open when browser search is not required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/gzh-ai-feed) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>
- [README.en.md](artifact/README.en.md) <br>
- [README.md (Chinese)](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, html, files, shell commands, configuration] <br>
**Output Format:** [Terminal status/table output plus a generated HTML daily report file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY. Reports are saved locally by default under ~/Downloads/QoderReports; optional subscription configures a recurring local scheduled job.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

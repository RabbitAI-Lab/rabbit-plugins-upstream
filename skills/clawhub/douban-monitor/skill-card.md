## Description: <br>
douban-monitor monitors Douban movie and TV sources for newly qualifying high-rated titles and generates local reports, JSON data, and a static web view. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juryory](https://clawhub.ai/user/juryory) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Media-focused users and developers use this skill to monitor Douban and TMDB sources for new high-rated films and series, review daily Markdown reports, and inspect generated JSON and static HTML output. <br>

### Deployment Geography for Use: <br>
Global, with best reliability from networks that can consistently access Douban and TMDB. <br>

## Known Risks and Mitigations: <br>
Risk: The configured automatic Git push mode can publish generated media-monitoring data to the configured remote repository. <br>
Mitigation: Use the skill only in repositories where those generated files are acceptable, or disable pushing with auto_git_push = false or DOUBAN_MONITOR_NO_PUSH=1. <br>
Risk: The skill sends media lookup requests to Douban and, when configured, TMDB. <br>
Mitigation: Configure TMDB credentials only when those lookups are acceptable, and keep credentials in environment variables rather than committed files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juryory/skills/douban-monitor) <br>
- [README.md](README.md) <br>
- [Implementation Notes](references/IMPLEMENTATION_NOTES.md) <br>
- [Example configuration](references/config.example.toml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown reports, JSON data files, static HTML pages, and concise text status updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated data, reports, and detail pages locally; when automatic Git push is enabled, it can commit and push generated monitoring data.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and changelog, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

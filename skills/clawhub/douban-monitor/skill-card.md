## Description: <br>
Monitors Douban film and TV lists for newly qualifying high-rated titles and produces daily reports, JSON data, and a static viewing page. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juryory](https://clawhub.ai/user/juryory) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media automation users use this skill to track recently popular Douban movies and series against rating and rating-count thresholds. It can run locally or with GitHub Actions to refresh reports, data files, and a static web view. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A default run can automatically commit and push generated data to the configured Git remote without per-run confirmation. <br>
Mitigation: Install in a dedicated repository or worktree, set auto_git_push=false or DOUBAN_MONITOR_NO_PUSH=1 unless pushing is intentional, review the Git remote and generated files before enabling push, and use least-privilege TMDB and GitHub credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juryory/skills/douban-monitor) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Implementation notes](artifact/references/IMPLEMENTATION_NOTES.md) <br>
- [Example configuration](artifact/references/config.example.toml) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, HTML, Shell commands, Configuration] <br>
**Output Format:** [Markdown reports, JSON data files, static HTML pages, and concise run guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local files under data/, detail/, and reports/; TMDB enrichment depends on optional credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

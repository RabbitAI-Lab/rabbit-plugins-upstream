## Description: <br>
绿联 NAS 智能影视助手 is a conversational home NAS media-management skill that routes media identification, web resource search, download tasks, and file organization after an initial environment check. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[54fanqie](https://clawhub.ai/user/54fanqie) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Home NAS users and operators use this skill from chat endpoints to identify media, search candidate resources, send downloads to their own qBittorrent or Xunlei setup, and organize completed files into a media library. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start media downloads and send search terms, candidate links, and download URLs to configured public sources, Xunlei Cloud, qBittorrent, local logs, and caches. <br>
Mitigation: Review candidate links before download, use only trusted downloader endpoints, and avoid sensitive search terms or URLs when external services are configured. <br>
Risk: The skill can move or delete NAS files with only partially enforced safeguards. <br>
Mitigation: Use a dedicated download inbox and media-library path, keep backups, inspect dry-run reports, and avoid purge-style cleanup until the planned changes are understood. <br>
Risk: The skill depends on local credentials, downloaders, paths, and Python dependencies being configured correctly before normal operation. <br>
Mitigation: Run the initial environment check, confirm required variables and mounted paths, and stop normal media actions until blocking configuration issues are fixed. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/54fanqie/nas-media-assistant) <br>
- [ClawHub skill page](https://clawhub.ai/54fanqie/skills/nas-media-assistant) <br>
- [SkillHub homepage](https://www.skillhub.cn/skills/user_2645d56b/nas-media-assistant) <br>
- [Human overview](docs/README.md) <br>
- [Lifecycle reference](references/lifecycle.md) <br>
- [Routing reference](references/routing.md) <br>
- [TMDB API settings](https://www.themoviedb.org/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration values, and structured status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute download and file-organization steps only after required environment checks and user confirmations described by the skill.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

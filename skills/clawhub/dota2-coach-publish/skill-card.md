## Description: <br>
Provides Chinese Dota 2 hero win-rate context, item build recommendations, gameplay guidance, skill details, and talent analysis using bundled local data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangjian1412](https://clawhub.ai/user/yangjian1412) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Dota 2 players and agent users use this skill to request Chinese-language hero build advice, lane and fight guidance, rank-segment win-rate context, skill data, and talent information. Maintainers can optionally run bundled refresh scripts to update local Dota data from public sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Dota-related triggers may activate the skill for general Dota 2 questions. <br>
Mitigation: Install and enable it only for users who want Chinese Dota 2 coaching and build guidance. <br>
Risk: Optional update scripts fetch public data from OpenDota, dota2.com.cn, and GitHub and rewrite bundled local databases. <br>
Mitigation: Use the bundled local data by default; run update scripts only after reviewing the scripts and accepting the network access and local file rewrite behavior. <br>
Risk: Dota 2 balance changes can make bundled gameplay and item recommendations stale. <br>
Mitigation: Check the skill version and data update notes before relying on recommendations for current patch play. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangjian1412/skills/dota2-coach-publish) <br>
- [OpenDota API](https://api.opendota.com/api) <br>
- [OpenDota heroStats endpoint](https://api.opendota.com/api/heroStats) <br>
- [OpenDota hero item popularity endpoint pattern](https://api.opendota.com/api/heroes/{hero_id}/itemPopularity) <br>
- [dotabase data repository](https://github.com/mdiller/dotabase) <br>
- [Dota 2 China datafeed](https://www.dota2.com.cn/datafeed/) <br>
- [Valve VPK file format reference](https://developer.valvesoftware.com/wiki/VPK_File_Format) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands] <br>
**Output Format:** [Chinese Markdown-style coaching responses with tables and optional bash commands for manual data refresh] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bundled local JSON data by default; optional update scripts fetch public Dota data and rewrite local databases when explicitly run.] <br>

## Skill Version(s): <br>
1.1.9 (source: frontmatter, README changelog, server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

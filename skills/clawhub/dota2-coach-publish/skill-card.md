## Description: <br>
Provides Dota 2 hero win-rate lookup, item-build recommendations, playstyle guidance, and skill and talent analysis from bundled game-data files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangjian1412](https://clawhub.ai/user/yangjian1412) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Dota 2 players and agent users use this skill to ask for hero win rates, item builds, lane guidance, teamfight priorities, skill details, and talent recommendations. It is best suited for gameplay coaching and planning based on the bundled local data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Dota-related trigger phrases may activate the skill for general Dota discussion where coaching output was not intended. <br>
Mitigation: Install it only for agents expected to provide Dota 2 advice, and treat generated recommendations as gameplay guidance rather than authoritative facts. <br>
Risk: Manual refresh scripts can overwrite local game-data JSON files. <br>
Mitigation: Use the bundled data by default; review script paths and keep backups before running refresh commands. <br>
Risk: Some helper scripts contain hard-coded OpenClaw workspace paths. <br>
Mitigation: Update paths for the local environment before executing those helper scripts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yangjian1412/skills/dota2-coach-publish) <br>
- [OpenDota API](https://api.opendota.com/api) <br>
- [dotabase Data Repository](https://github.com/mdiller/dotabase) <br>
- [Valve VPK File Format](https://developer.valvesoftware.com/wiki/VPK_File_Format) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands] <br>
**Output Format:** [Markdown responses with tables, bullets, and occasional shell command snippets for data refresh workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bundled Dota 2 datasets by default; manual refresh scripts can update local game-data JSON files.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

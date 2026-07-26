## Description: <br>
Parse and analyze GPX route files for trail running, cycling, hiking, and race planning. Use when the user provides or references a .gpx file and asks for route distance, elevation gain/loss, waypoint/CP extraction, segment stats, terrain difficulty, pacing tables, roadbooks, cutoff planning, or checkpoint arrival estimates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[forrestisrunning](https://clawhub.ai/user/forrestisrunning) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, outdoor athletes, coaches, and race planners use this skill through an agent to parse GPX route files, summarize distance, elevation, checkpoints, and segments, and create practical pacing tables or roadbook guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GPX files can expose precise route and location history. <br>
Mitigation: Run the helper only on GPX files the user intends to share with the agent, and avoid disclosing route details beyond the user's requested analysis. <br>
Risk: Generated pacing, cutoff, or route strategy advice may be unsuitable for real outdoor conditions. <br>
Mitigation: Review generated route and pacing guidance before relying on it outdoors, accounting for weather, terrain, daylight, altitude, and personal fitness. <br>


## Reference(s): <br>
- [Read GPX ClawHub Page](https://clawhub.ai/forrestisrunning/skills/read-gpx) <br>
- [Read GPX skill repository link from README](https://github.com/forrestIsRunning/read-gpx-skill.git) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with optional plain-text CLI summaries and JSON parser output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local GPX files may contain precise location history; route and pacing advice should be reviewed before outdoor use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

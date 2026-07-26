## Description: <br>
Garmer extracts health and fitness data from Garmin Connect, including activities, sleep, heart rate, stress, steps, body composition, hydration, and respiration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[garrza](https://clawhub.ai/user/garrza) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and health insight agents use Garmer to retrieve Garmin Connect activity, sleep, heart rate, stress, step, and body composition data for personal health analysis and AI assistant integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Garmer accesses sensitive Garmin health and fitness data and stores Garmin OAuth tokens locally. <br>
Mitigation: Use interactive login, protect the token directory and exported JSON files, and avoid sharing generated health exports without review. <br>
Risk: The skill includes a self-update command that can change local code through git. <br>
Mitigation: Run the update command only when the repository remote is trusted and the resulting code changes can be reviewed before continued use. <br>


## Reference(s): <br>
- [Garmer API Reference](artifact/references/REFERENCE.md) <br>
- [Garmer Skill Page](https://clawhub.ai/garrza/skills/garmer) <br>
- [garth Garmin Connect Authentication Library](https://github.com/matin/garth) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, Python code examples, and JSON output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that authenticate to Garmin Connect, read locally stored tokens, and export health data as JSON.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

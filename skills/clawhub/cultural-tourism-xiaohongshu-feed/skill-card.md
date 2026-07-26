## Description: <br>
Searches Xiaohongshu cultural tourism posts, ranks popular content by engagement, clusters results by topic, and generates a local HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, tourism marketers, and researchers use this skill to monitor Xiaohongshu cultural tourism trends, inspect category counts, and open a generated HTML report for detailed posts and links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan verdict is suspicious because subscription mode can persist scheduled jobs, handle API credentials insecurely, and use unsafe shell commands. <br>
Mitigation: Install only from a trusted publisher and avoid subscription mode until the scheduled command, credential handling, and removal behavior can be reviewed. <br>
Risk: The skill reads REDFOX_API_KEY, contacts RedFox, writes local HTML reports, and may open generated files in a browser. <br>
Mitigation: Use a scoped and revocable API key, avoid exposing it in prompts or logs, choose an appropriate output directory, and review generated reports before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/cultural-tourism-xiaohongshu-feed) <br>
- [RedFoxHub API keys](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk?source=github) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown summary with category counts, terminal output, and generated local HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY, contacts RedFox, writes local HTML reports, may open the report in a browser, and can optionally install scheduled jobs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

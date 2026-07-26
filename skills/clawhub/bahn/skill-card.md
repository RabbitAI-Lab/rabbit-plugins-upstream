## Description: <br>
Search Deutsche Bahn train connections using the bahn-cli tool. Use when you need to find train connections between German stations, check departure times, or help with travel planning. Works with station names like "Berlin Hbf", "München", "Hannover". <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobiasbischoff](https://clawhub.ai/user/tobiasbischoff) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Travel-planning users and agents use this skill to search Deutsche Bahn connections between German stations, including departure times, platforms, duration, changes, and train numbers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks the agent to run setup commands for a separate local Node.js project at ~/Code/bahn-cli. <br>
Mitigation: Install only when that path is the intended train-search project and review its package.json and lockfile before running npm install. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

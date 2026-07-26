## Description: <br>
Local-first chart generation engine for trends, comparisons, distributions, and quick visual explanations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ProjectSnowWork](https://clawhub.ai/user/ProjectSnowWork) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and other agent users use this skill to choose simple chart types, generate local PNG charts from inline data, and review saved chart history for reports or decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Chart inputs, generated images, and chart history are persisted locally under ~/.openclaw/workspace/memory/chart. <br>
Mitigation: Use non-sensitive chart data unless local persistence in that folder is acceptable, and remove generated history or files when they are no longer needed. <br>
Risk: The chart scripts depend on the local Python 3 and matplotlib installation. <br>
Mitigation: Install Python 3 and matplotlib from trusted sources and run the skill in an environment with expected local file permissions. <br>


## Reference(s): <br>
- [Chart Philosophy](references/philosophy.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated PNG chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates PNG chart files and local JSON chart history under ~/.openclaw/workspace/memory/chart.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill.json and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

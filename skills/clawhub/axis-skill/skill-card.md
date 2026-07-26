## Description: <br>
Axis is a Chinese gaokao admissions-advising skill that helps with college entrance exam applications, major selection, school recommendations, volunteer application strategy, and AI-era major survival analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ares0x](https://clawhub.ai/user/ares0x) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External students, families, and admissions advisers use Axis to collect student profile facts, explore Holland-style career interests, evaluate candidate majors, and generate China-focused admissions guidance and survival reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants shell-command authority for admissions workflow commands. <br>
Mitigation: Install only from a trusted publisher and review commands before execution. <br>
Risk: The workflow can persist student advising data in local session and report files. <br>
Mitigation: Avoid sharing sensitive student details unless the user understands where files are saved and how to remove them. <br>
Risk: The package includes instructions but not the referenced runner, data files, or safe execution wrapper. <br>
Mitigation: Verify required scripts and data sources are present and trustworthy before relying on generated recommendations. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/ares0x/axis-skill) <br>
- [ClawHub skill page](https://clawhub.ai/ares0x/skills/axis-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and report or snapshot file path instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to create local student session snapshots and survival reports under workspace/sessions/{uid}/.] <br>

## Skill Version(s): <br>
2.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

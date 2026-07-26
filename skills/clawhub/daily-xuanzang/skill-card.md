## Description: <br>
Daily Xuanzang helps an agent deliver progressive bilingual readings of the Great Tang Records on the Western Regions with tracked progress, translations, route-map guidance, and optional voice narration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yumyumtum](https://clawhub.ai/user/yumyumtum) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run a daily illustrated reading workflow for Xuanzang's journey, generating a lecture segment with translation, historical context, map guidance, progress tracking, and optional audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persists reading progress and replay artifacts locally. <br>
Mitigation: Tell users where progress and replay files are written and let them inspect, back up, or delete those files. <br>
Risk: Voice generation depends on a referenced audio helper script that is not bundled in the artifact. <br>
Mitigation: Inspect or provide the helper script before enabling voice output; skip voice if the script is unavailable. <br>
Risk: Original historical passages may include biased or culturally dated descriptions. <br>
Mitigation: Frame translated passages as historical source material and add context in the lecture. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yumyumtum/skills/daily-xuanzang) <br>
- [README](README.md) <br>
- [Structure Reference](references/structure.md) <br>
- [Lecture Style Guide](references/style-guide.md) <br>
- [Example Lecture](assets/example-lecture-001.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown lecture text with inline shell commands and structured generation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to generate route-map images, optional scene art, optional voice narration, and local progress or replay files.] <br>

## Skill Version(s): <br>
0.2.0 (source: evidence.release.version and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

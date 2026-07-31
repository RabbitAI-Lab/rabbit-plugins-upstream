## Description: <br>
将会议逐字稿或录音转写文本转化为手机端可直接转发的 SVG 会议纪要卡片，并自动转为 PNG 方便分享。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, external collaborators, and operations teams use this skill to convert multi-party meeting transcripts into shareable visual meeting minutes with decisions, owners, timelines, and action items. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The PNG converter may automatically install a Python rendering package into the host environment when a dependency is missing. <br>
Mitigation: Run the skill in a virtual environment or container, or preinstall reviewed and pinned rendering dependencies before using PNG conversion. <br>
Risk: Meeting transcripts can contain sensitive business information even when processing is local. <br>
Mitigation: Use approved local workspaces, review transcript handling requirements, and share generated SVG/PNG files only with intended recipients. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/maojiebc/skills/majia-meeting-svg) <br>
- [Project Homepage](https://github.com/maojiebc/majia-meeting-svg) <br>
- [Example Meeting Cards](https://github.com/maojiebc/majia-meeting-svg/tree/main/references/examples) <br>
- [README.en.md](README.en.md) <br>
- [llms.txt](llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Files] <br>
**Output Format:** [SVG and PNG files with a concise text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [PNG conversion defaults to 2x scale; generated content should preserve exact meeting facts, dates, numbers, owners, and unresolved items.] <br>

## Skill Version(s): <br>
1.1.13 (source: SKILL.md metadata.version and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

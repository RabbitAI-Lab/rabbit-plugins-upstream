## Description: <br>
基于腾讯会议(tmeet)培训会议的录制转写，把冗长转写稿自动整理为带章节结构、要点提炼与自测题的培训手册。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golgys0621](https://clawhub.ai/user/golgys0621) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, trainers, and team leads use this skill to turn Tencent Meeting training transcripts or local transcript files into reusable Markdown training handbooks with chapters, key points, and self-test questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Training transcripts or minutes may contain internal or sensitive meeting content. <br>
Mitigation: Use only meeting IDs or local files the user is authorized to access, and review the generated handbook before sharing. <br>
Risk: Generated chapters, key points, or self-test questions may omit context or be unsuitable for formal assessment. <br>
Mitigation: Treat self-test questions as study aids and have a subject-matter reviewer approve material used for official training or exams. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golgys0621/skills/training-notes-skill) <br>
- [Training handbook template](references/training_template.md) <br>
- [Local training transcript example](examples/培训转写.md) <br>
- [Generated training handbook example](examples/培训手册.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown training handbook with chapters, extracted key points, and self-test questions; optional shell command for local file processing.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes selected Tencent Meeting training transcripts or authorized local .md/.txt transcript files.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

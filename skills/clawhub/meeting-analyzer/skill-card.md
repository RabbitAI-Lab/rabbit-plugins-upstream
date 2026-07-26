## Description: <br>
Analyzes Tencent Meeting or Feishu Meeting transcripts from a meeting link and produces structured analysis, summary diagrams, and Markdown or HTML meeting reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and knowledge workers use this skill to turn Tencent Meeting or Feishu Meeting transcripts into structured JSON, drawio summaries, Markdown reports, and HTML meeting reports for review or sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting transcripts, participants, decisions, and action items may contain private or confidential information. <br>
Mitigation: Confirm permission to process the meeting content and store or share generated reports only under the user's organization policies. <br>
Risk: The skill may rely on Tencent Meeting, Feishu or Lark CLI authorization and writes generated reports to local storage. <br>
Mitigation: Install and authorize only the required platform CLI tools, review their access scope, and choose an appropriate local output location. <br>
Risk: Transcript quality depends on the meeting platform ASR and optional analysis settings, so summaries or extracted decisions may be incomplete. <br>
Mitigation: Review generated JSON, reports, and action items against the source transcript before relying on or distributing them. <br>


## Reference(s): <br>
- [Source repository](https://github.com/samonysh/meeting-analyzer) <br>
- [ClawHub skill listing](https://clawhub.ai/samonysh/skills/meeting-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and descriptions of generated JSON, drawio, Markdown, HTML, and image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local meeting analysis files, including structured JSON, drawio diagrams, Markdown and HTML reports, and optional snapshots when video input is provided.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

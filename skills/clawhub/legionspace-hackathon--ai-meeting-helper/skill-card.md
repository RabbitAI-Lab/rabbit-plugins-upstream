## Description: <br>
AI Meeting Helper converts meeting recordings into structured notes with transcripts, summaries, action items, decisions, and to-dos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to process single or batch meeting recordings into structured notes for review, follow-up, and distribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting recordings and transcript text are sent to OpenAI for transcription and summarization. <br>
Mitigation: Use only for meetings where organizational policy and participant consent permit third-party processing; avoid confidential, regulated, or consent-sensitive content unless approved. <br>
Risk: Generated meeting notes may omit, misstate, or over-interpret discussion details. <br>
Mitigation: Review generated summaries, decisions, and action items against the source meeting before sharing or using them for follow-up. <br>
Risk: Install and uninstall behavior creates configuration, backup, and log paths and can delete those files when requested. <br>
Mitigation: Review the configured paths and uninstall prompt before deleting configuration, backup, or log data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/ai-meeting-helper) <br>
- [Publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown, plain text, or JSON meeting notes, with shell command examples and OpenAI API key configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENAI_API_KEY; supports preview mode, batch audio processing, file output, and optional backups.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, skill frontmatter, and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

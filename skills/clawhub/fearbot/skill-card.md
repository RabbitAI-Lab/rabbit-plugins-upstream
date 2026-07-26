## Description: <br>
FearBot provides a CBT-based therapy companion for anxiety, depression, stress, and trauma, with validated assessments, session tracking, thought records, differential diagnosis, and crisis detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samoppakiks](https://clawhub.ai/user/samoppakiks) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use this skill as a local CBT support and journaling companion for mild-to-moderate anxiety, depression, stress, and trauma symptoms. It is intended to supplement, not replace, licensed mental-health care or emergency crisis support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores sensitive mental-health history locally and can export therapy records. <br>
Mitigation: Confirm the SQLite database and export paths before use, avoid synced or shared folders, and protect or delete exported Markdown files when no longer needed. <br>
Risk: Users may mistake the tool for licensed care or emergency crisis support. <br>
Mitigation: Use it only as support or journaling, seek a qualified professional for serious or persistent concerns, and contact emergency services or crisis lines during a crisis. <br>
Risk: Broad activation and always-on crisis monitoring can cause sensitive messages to be interpreted as therapy context. <br>
Mitigation: Review activation phrases and keep therapy sessions intentional, especially on shared machines or shared agent contexts. <br>


## Reference(s): <br>
- [Assessment Administration Prompts](references/assessment-items.md) <br>
- [Crisis Detection & Response Layer](references/crisis-layer.md) <br>
- [Session Context Assembly Template](references/session-context-template.md) <br>
- [Base Therapist System Prompt](references/therapist-prompt.md) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [International Association for Suicide Prevention Crisis Centres](https://www.iasp.info/resources/Crisis_Centres/) <br>
- [Befrienders Worldwide](https://www.befrienders.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Conversational text and Markdown, with optional shell commands for local SQLite session storage and Markdown exports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores therapy history locally in SQLite and can export therapy records as Markdown.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence, SKILL.md frontmatter, skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

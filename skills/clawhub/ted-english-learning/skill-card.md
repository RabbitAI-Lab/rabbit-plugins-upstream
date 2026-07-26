## Description: <br>
Converts TED talk PDFs or pasted English text into bilingual study notes, vocabulary lists, summaries, sentence analysis, reading questions, and Obsidian Canvas mind maps for English learning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiao2769433](https://clawhub.ai/user/xiao2769433) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners and agents use this skill to transform TED talk PDFs or pasted English text into structured bilingual English-learning materials. It supports note generation, vocabulary review, content summaries, sentence analysis, exam-style reading questions, and Obsidian Canvas summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates and updates files under the current working directory, including English/English.md and files under English/TED. <br>
Mitigation: Use the skill from a dedicated study-notes folder and review target paths before running it. <br>
Risk: Generated Obsidian Canvas files may fail to open if the JSON content is malformed. <br>
Mitigation: Validate Canvas JSON before use and preserve the required node structure and color values. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/xiao2769433/ted-english-learning) <br>
- [ClawHub skill page](https://clawhub.ai/xiao2769433/skills/ted-english-learning) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown notes and Obsidian Canvas JSON files, with shell commands for PDF extraction when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated notes under English/TED, Canvas files under English/TED/CANVAS, and updates English/English.md in the current working directory.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

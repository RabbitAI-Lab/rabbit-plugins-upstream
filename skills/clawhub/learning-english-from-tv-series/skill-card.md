## Description: <br>
DramaLex helps Chinese-speaking English learners turn TV episodes or films into a guided study loop with CEFR diagnosis, vocabulary priming, listening tasks, transcript annotation, speaking and writing practice, review, and exportable study materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yinjianheng](https://clawhub.ai/user/yinjianheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Chinese-speaking English learners use this skill to convert a chosen TV episode or film into a structured English-learning workflow. The skill supports study-plan generation, subtitle-based exercises, vocabulary cards, listening and speaking drills, writing tasks, and review artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad subtitle retrieval and under-scoped network behavior. <br>
Mitigation: Prefer user-supplied lawful subtitles, review fetched sources before use, and avoid gated, protected, or access-controlled sites. <br>
Risk: The security guidance notes that online TTS may send selected text to a third party. <br>
Mitigation: Use local TTS where available, or require explicit user acceptance before using online TTS. <br>
Risk: The skill can write local study artifacts and may enable reminders. <br>
Mitigation: Run it in a user-approved working directory and keep reminders disabled unless the user explicitly wants them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yinjianheng/skills/learning-english-from-tv-series) <br>
- [Subtitle Legal Boundaries](references/SUBTITLE_LEGAL.md) <br>
- [TTS Note](references/TTS_NOTE.md) <br>
- [Anki Guide](references/ANKI_GUIDE.md) <br>
- [Cross-Agent Guide](references/CROSS_AGENT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON schemas, Python and shell command examples, and generated study artifacts such as HTML, Anki, Excel, Word, Markdown, and CORE JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local study artifacts and optionally use local or online TTS; subtitle retrieval should follow the security and legal guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

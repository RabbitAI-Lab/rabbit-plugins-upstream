## Description: <br>
Generates personalized English listening practice materials matched to a learner's vocabulary, interests, and sticking points, with fallback guidance when audio or persistent memory features are unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students and English-learning assistants use this skill to create level-appropriate listening passages, comprehension checks, vocabulary notes, and follow-up coaching based on learner profiles and interests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read or update learner profiles, vocabulary records, listening history, reminders, and reports without clearly documented opt-in controls. <br>
Mitigation: Review before installation, require explicit learner or guardian consent, and confirm how stored vocabulary, reminders, and progress history can be viewed, disabled, or deleted. <br>
Risk: The skill's true listening workflow depends on audio generation, speed control, and persistent memory that may not be available in every agent environment. <br>
Mitigation: Tell learners when audio or memory features are unavailable and use the documented text-based fallback only as a temporary comprehension exercise. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer) <br>
- [Listening topic templates and material generation guide](references/listening-topic-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style tutoring responses with listening passages, vocabulary notes, comprehension questions, diagnostics, and progress summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on platform TTS, speed control, learner-profile memory, and reminder capabilities.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

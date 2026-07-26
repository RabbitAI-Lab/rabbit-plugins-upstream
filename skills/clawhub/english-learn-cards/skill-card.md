## Description: <br>
Flashcard-based English vocabulary learning with SQLite + SRS. Works with any chat platform when paired with an OpenClaw agent prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[racymind](https://clawhub.ai/user/racymind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Learners and language-learning agents use this skill to create, review, and grade English vocabulary flashcards across chat platforms. It supports local spaced-repetition study workflows with deterministic helper commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional audio lookup can send requested headwords or phrases to Cambridge Dictionary. <br>
Mitigation: Avoid --fill-audio or --audio-auto for sensitive words or phrases unless that external lookup is acceptable. <br>
Risk: The local SQLite database may contain personal study data. <br>
Mitigation: Keep the database local and do not commit it with published skill files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/racymind/skills/english-learn-cards) <br>
- [Agent prompt template](prompt-examples/AGENT_PROMPT_TEMPLATE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style chat text with helper CLI commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local SQLite vocabulary database; optional pronunciation lookup may contact Cambridge Dictionary.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

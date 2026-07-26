## Description: <br>
Interactive Japanese learning assistant. Supports vocabulary, grammar, quizzes, roleplay, PDF/DOCX material parsing for study/homework help, and OCR translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chndranndr](https://clawhub.ai/user/chndranndr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External learners and tutors use this skill to practice beginner Japanese vocabulary and grammar, translate Japanese text or images, quiz known material, and work through PDF or DOCX course materials with guided explanations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF parsing sends uploaded PDF content to Google Gemini. <br>
Mitigation: Use PDF parsing only with documents that are approved for external processing, and avoid confidential or sensitive materials. <br>
Risk: Study material and extracted learnings may be retained in local reference markdown files. <br>
Mitigation: Review updated reference files after material ingestion and remove sensitive, unwanted, or inaccurate retained notes. <br>


## Reference(s): <br>
- [Japanese Tutor on ClawHub](https://clawhub.ai/chndranndr/skills/japanese-tutor) <br>
- [Japanese Grammar - Beginner Level](references/grammar.md) <br>
- [Lesson 2 Grammar](references/grammar_lesson2.md) <br>
- [Pelajaran 1: Kalimat Dasar & Kosakata Profesi](references/lesson_1.md) <br>
- [Japanese Vocabulary - Beginner Level (N5)](references/vocab.md) <br>
- [Lesson 2 Vocabulary](references/vocab_lesson2.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, code, shell commands] <br>
**Output Format:** [Markdown text with optional shell commands and updates to local reference files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call local parsing scripts; PDF parsing requires GEMINI_API_KEY and sends PDF content to Google Gemini.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

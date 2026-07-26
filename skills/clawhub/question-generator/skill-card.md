## Description: <br>
AI Question Generator helps agents create multi-format educational quizzes from topics, source material, or study goals, including answers, explanations, Bloom taxonomy labels, quality checks, and optional interactive HTML output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, trainers, and learning-content developers use this skill to generate structured practice questions, exams, and quiz papers for K12, higher education, and vocational training. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local Python script and writes an HTML quiz file. <br>
Mitigation: Review the generated command before execution and choose an explicit output path inside the intended workspace. <br>
Risk: Embedding quiz JSON directly in a shell command can expose quoting or command-line handling problems. <br>
Mitigation: Prefer piping quiz JSON through stdin, as recommended by the security guidance. <br>
Risk: Untrusted study material could become unsafe when rendered into inline JavaScript in the generated HTML. <br>
Mitigation: Avoid untrusted inputs unless the renderer is fixed to safely encode data for inline JavaScript. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/skills/question-generator) <br>
- [Bloom taxonomy question guide](references/bloom-taxonomy.md) <br>
- [Question type design specifications](references/question-types.md) <br>
- [Question quality checklist](references/quality-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with structured quiz JSON and optional interactive HTML file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can render quiz JSON into a local HTML file through scripts/generate_quiz.py.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

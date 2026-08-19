## Description:

Human Level Up helps an agent extract core learning points from user-provided material, explain them plainly, generate quiz challenges, compare answers in a Turing-reversal exercise, and track learning progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-acheng](https://clawhub.ai/user/ai-acheng)

### License/Terms of Use:

MIT-0

## Use Case:

Learners, students, professionals, and developers use this skill to turn documents, code, papers, or conversation history into concise learning modules and practice questions. It is suited for self-study workflows where the agent should teach, test understanding, give feedback, and maintain simple progress signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional bookmarklet, Docker, and serverless examples can send selected or uploaded content to external services.

Mitigation: Avoid those deployment examples for private, regulated, or proprietary documents unless the endpoint or image has been inspected and approved.

Risk: The workflow is primarily Chinese-language and may be unsuitable for teams expecting English-only learning materials.

Mitigation: Confirm language expectations before installation or adapt the prompts for the target audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-acheng/skills/human-level-up)
- [Server-resolved GitHub provenance](https://github.com/AI-aCheng/human-level-up)
- [README](artifact/README.md)
- [Skill definition](artifact/skill.md)
- [Prompt behavior](artifact/prompt.md)
- [Examples](artifact/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown conversation output with optional JSON from helper scripts and inline shell or code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Chinese-language explanations, multiple-choice questions, answer feedback, point totals, and local progress records.]

## Skill Version(s):

3.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

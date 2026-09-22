## Description:

Diagnoses and rewrites Chinese prose that sounds machine-generated, with genre-specific guidance for preserving facts, tone, citations, and formal constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[junci003](https://clawhub.ai/user/junci003)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language writers, editors, and agents use this skill to identify AI-sounding patterns and rewrite Chinese public copy, formal text, course material, resumes, email, product copy, and similar prose before publication. It is intended to make Chinese text read more human while preserving supplied facts, numbers, citations, and author-specific style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate on broad Chinese pre-publication editing requests and may change tone or structure more than intended.

Mitigation: Confirm the target genre and rewrite strength before substantial edits; use lighter rewrites for formal, legal, cited, or policy-constrained text.

Risk: Humanizing prose can accidentally weaken factual precision, citations, legal wording, or formal style.

Mitigation: Preserve every supplied fact, number, citation, quote, legal phrase, and policy expression; request missing real details instead of inventing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/junci003/skills/zh-humanizer)
- [中文 AI 味清单](references/tells.md)
- [改写手法手册](references/rewrite-playbook.md)
- [分场景档位](references/by-genre.md)
- [blader/humanizer](https://github.com/blader/humanizer)
- [obra/superpowers](https://github.com/obra/superpowers)
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with rewritten Chinese prose, diagnosis notes, change summaries, and requests for missing source material when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not execute code or access credentials; may ask for author samples or real details when the requested rewrite would otherwise require inventing facts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

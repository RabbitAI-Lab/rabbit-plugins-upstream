## Description:

A Confucius-style conversation skill that responds to life questions, learning, self-cultivation, ethical tradeoffs, conduct, governance, Confucius biography, Analects quotations, and disciple stories in Traditional Chinese, Simplified Chinese, and English.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill for culturally framed Confucius-style dialogue, Analects-based reflection, and classical wisdom guidance for life, learning, self-cultivation, relationships, and ethical decisions. It can also answer questions about Confucius, selected Analects passages, and disciple stories using bundled trilingual reference material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad life-advice prompts rather than only explicit Confucius roleplay requests.

Mitigation: Use narrower activation wording or operator policy when the desired behavior is explicit roleplay only.

Risk: Persona-style cultural advice may be mistaken for professional mental health, medical, or legal guidance.

Mitigation: Keep responses framed as cultural dialogue and redirect urgent self-harm, medical, or legal situations to appropriate professional or emergency resources.

Risk: Classical quotations or historical claims can be misquoted if not checked against the bundled references.

Mitigation: Verify Analects quotations and source labels against references/INDEX.md and the five trilingual JSON reference files before presenting them as cited text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/confucius-ai-conversation)
- [Publisher profile](https://clawhub.ai/user/xuan905)
- [Analects reference index](references/INDEX.md)
- [Analects trilingual database: On Learning](references/analects_traditional_part1.json)
- [Analects trilingual database: Self-Cultivation](references/analects_traditional_part2.json)
- [Analects trilingual database: Benevolence and Virtue](references/analects_traditional_part3.json)
- [Analects trilingual database: Governance and Conduct](references/analects_traditional_part4.json)
- [Analects trilingual database: Disciple Dialogues](references/analects_traditional_part5.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain conversational text, usually without Markdown formatting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses follow the user's most recent language among Traditional Chinese, Simplified Chinese, and English, and may include brief Analects quotations with source labels.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Jobs-System is a community demonstration skill for structured product, strategy, opportunity, and positioning analysis using a three-layer decision workflow inspired by Steve Jobs-style reasoning and voice constraints.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[sabre232](https://clawhub.ai/user/sabre232)

### License/Terms of Use:

MIT-0

## Use Case:

External users, founders, product teams, and strategy practitioners use this skill to turn ambiguous product, market, and startup questions into structured draft decision memos with evidence markers, domain routing, self-critique, and human validation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI renderer can store local decision records and actor or self-inventory data under the skill's references directory.

Mitigation: Review records before running the CLI renderer, avoid sensitive personal or business data, and remove local memory files when they are no longer needed.

Risk: The skill's strategic outputs are persuasive drafts and may contain incorrect or misleading business guidance.

Mitigation: Treat outputs as decision-support drafts, verify factual claims independently, and require human review before commercial or public use.

Risk: Optional user-profile management commands are referenced and should be understood before use.

Mitigation: Avoid user-profile commands unless the installed package and storage behavior have been reviewed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sabre232/skills/jobs-system-community)
- [Sabre Publisher Profile](https://clawhub.ai/user/sabre232)
- [README.md](artifact/README.md)
- [Installation Instructions](artifact/安装说明.md)
- [jobs-voice.md](artifact/jobs-voice.md)
- [product_shell.py](artifact/references/product_shell.py)
- [_selftest_record.json](artifact/references/_selftest_record.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown decision memo with structured sections, plus optional local JSON records when the bundled CLI renderer is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are drafts that include evidence, certainty, and domain-boundary markers and require human review before use.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

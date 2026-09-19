## Description:

KnowPitch breaks a knowledge domain into a football formation for structured learning, producing an SVG formation diagram, ELI5-style player cards, and a tactics board.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyabao](https://clawhub.ai/user/iyabao)

### License/Terms of Use:

MIT-0

## Use Case:

Learners, teachers, and study-prep users use KnowPitch to organize knowledge-type topics into a visual formation, learning path, and plain-language explanation. It is not intended for precise data reports, code debugging, counseling, or quick fact lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce misleading learning material for precise factual or fast-changing topics if sources are not checked first.

Mitigation: Use it for educational topic organization and verify sources before generating or accepting fact-sensitive explanations.

Risk: The skill defaults to Chinese output, which may not match every user's language expectations.

Mitigation: Set the language parameter or ask for a specific output language when needed.

Risk: The skill creates local JSON and SVG files during diagram generation.

Mitigation: Review generated file paths and outputs before sharing or deploying the result.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/IYABAO/knowpitch/tree/main/skills/knowpitch)
- [ClawHub skill page](https://clawhub.ai/iyabao/skills/knowpitch)
- [Formation selection rules](artifact/references/formations.md)
- [Position role mapping](artifact/references/positions.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Code, Shell commands, Guidance]

**Output Format:** [Markdown learning card with local SVG diagram output and JSON diagram input]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output language is Chinese unless the user requests another language.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact metadata version is 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

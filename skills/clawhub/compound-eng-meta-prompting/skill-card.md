## Description:

Provides structured decision modifiers such as /think, /verify, /adversarial, /edge, /confidence, and /assumptions to stress-test conclusions, evidence, assumptions, alternatives, and edge cases before important decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and technical decision-makers use this skill to request structured reviews of ambiguous plans, architecture choices, security-sensitive work, and other decisions where assumptions, alternatives, confidence, or failure modes should be explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change answer structure in common technical conversations, including automatic structured review patterns.

Mitigation: Use it where structured design, security, validation, and architecture review is desired; avoid or scope it where users prefer these formats only when explicitly requested.

Risk: Formal decision-record formats can make uncertain conclusions appear more authoritative than the underlying evidence supports.

Mitigation: Review assumptions, evidence, confidence labels, and counterarguments before relying on outputs for important design, architecture, or security decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-meta-prompting)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown, plain text, JSON code blocks, and comparison tables depending on the requested modifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include decision records, confidence tiers, assumptions, counterarguments, edge cases, and verification markers.]

## Skill Version(s):

4.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

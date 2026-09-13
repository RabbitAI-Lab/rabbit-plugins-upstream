## Description:

Measure and safely reduce always-loaded agent instruction context in characters and tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to measure recurring prompt cost from always-loaded instruction files and plan reductions without weakening authority, safety, or meaning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Editing always-loaded instruction files can change production agent behavior or weaken authority, safety, or rule availability.

Mitigation: Require explicit edit scope, map rule authority before moving text, preserve higher-precedence rules, and run semantic review plus prompt-assurance regressions.

Risk: Exact token counting sends selected file contents to a tokenizer service.

Mitigation: Use only a trusted loopback tokenizer that does not retain requests, or rely on the default character-based estimates.

Risk: Reports can reveal workspace identity or instruction-derived content when content display is explicitly enabled.

Mitigation: Keep default redaction enabled unless there is explicit local intent, and redact output before sharing.

## Reference(s):

- [Method and measurements](references/method.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default reports redact workspace identity, selected file labels, headings, duplicate lines, and path prefixes; exact token counts require a trusted loopback tokenizer.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

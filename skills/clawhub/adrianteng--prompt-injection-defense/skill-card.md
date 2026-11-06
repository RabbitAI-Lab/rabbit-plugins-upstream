## Description:

Hardens agent sessions against prompt injection from untrusted content with content tagging, scanning, memory write guardrails, and canary detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adrianteng](https://clawhub.ai/user/adrianteng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to reduce prompt-injection risk when agents ingest web results, emails, downloads, PDFs, RSS feeds, API responses, or other external text. It provides scanning and handling guidance before external content can influence actions or persistent memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write persistent agent memory, including long-term memory.

Mitigation: Use only in a controlled workspace, review writes before promotion, and avoid long-term memory writes until source validation, escaping, and sensitive-data redaction are fixed.

Risk: Untrusted or malformed content may bypass the skill's own guardrails.

Mitigation: Review before installing, treat scanner output as one layer of defense, and keep explicit user approval requirements for actions based on external content.

Risk: External content could influence script arguments such as source, target, or threshold if those values are not controlled.

Mitigation: Keep source, target, and threshold values under trusted operator control and validate thresholds before relying on memory-write decisions.

## Reference(s):

- [Canary Patterns - Prompt Injection Detection](artifact/references/canary-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, JSON, Files]

**Output Format:** [Markdown guidance with bash examples; scripts emit JSON scan or write status and may create Markdown memory or quarantine files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bash and python3. The memory-write helper can append to daily or long-term memory files or quarantine suspicious content.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

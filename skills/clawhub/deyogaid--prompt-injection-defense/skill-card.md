## Description:

Harden agent sessions against prompt injection from untrusted content. Use when the agent reads web search results, emails, downloaded files, PDFs, or any external text that could contain adversarial instructions. Provides content scanning, memory write guardrails (scan → lint → accept or quarantine), untrusted content tagging, and canary detection. Also use when setting up new tools that ingest external content (email checkers, RSS readers, web scrapers).

This skill is ready for commercial/non-commercial use.

## Publisher:

[deyogaid](https://clawhub.ai/user/deyogaid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect external text for prompt-injection attempts and to apply guardrails when adding that text to agent memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hostile instructions from external text may be preserved in lasting agent memory.

Mitigation: Review memory-writing behavior before installation, require review before external text enters lasting memory, and retain untrusted-content labels. Treat normalized text as unverified, not as safe.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/deyogaid/skills/prompt-injection-defense)
- [Canary Patterns — Prompt Injection Detection](references/canary-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON, Markdown]

**Output Format:** [Markdown guidance, Bash commands, Python code, and JSON scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The memory workflow quarantines content at medium or higher severity for review.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

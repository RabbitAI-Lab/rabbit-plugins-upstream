## Description:

LYGO Context Guard is a local Python preflight helper that estimates token usage, redacts likely secrets, compacts large context inputs deterministically, and gates model-bound content against token budgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers and agent operators use this skill before re-injecting tool dumps, logs, files, or long chat history into a model. It helps reduce context size, avoid obvious secret exposure, and enforce token budgets with local deterministic commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read any user-supplied path passed with --file and print processed content to stdout.

Mitigation: Run it only on content intended for agent processing, review stdout before reinjection, and avoid passing sensitive files that are outside the task scope.

Risk: Secret redaction is best-effort pattern matching and may miss credentials or sensitive values.

Mitigation: Treat redaction as a preflight guardrail rather than a compliance scanner, and keep normal secret-handling controls in place.

Risk: Token estimates are heuristic and may not match a model provider's exact tokenizer or billing count.

Mitigation: Use conservative budgets, lower max-chars when over budget, and split large inputs when the budget gate exits over limit.

Risk: Optional preflight reports can write local output when --write and --i-consent are used.

Mitigation: Keep report writes consent-gated and under the skill state/ directory as documented.

## Reference(s):

- [Security Notes](references/SECURITY.md)
- [Quickstart](examples/quickstart.md)
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-context-guard)
- [Homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-context-guard)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [CLI stdout with JSON summaries and redacted or compacted text; optional local JSON preflight report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local processing; token estimates are heuristic; optional report writes require explicit consent and stay under state/.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

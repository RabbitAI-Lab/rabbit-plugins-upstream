## Description:

Compares multiple contracts from the same template by aligning clauses, identifying missing or extra clauses, and summarizing clause-text differences with original evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, procurement, audit, and operations users can compare contracts signed from the same template to find missing clauses and clause text changes. The skill is intended as a local mechanical comparison aid and does not provide legal advice or determine whether a clause is valid or favorable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports a suspicious security verdict because the free contract comparison tool also directs users toward an external install and paid purchase flow.

Mitigation: Use the local comparison flow only unless you intentionally want the paid flow; independently verify the package, source, version, and newly installed skill instructions before running the referenced npx install command.

Risk: The skill compares clause text but does not provide legal advice, validate clause enforceability, verify signatures or seals, or assess whether a clause is favorable.

Mitigation: Treat results as comparison evidence for human review and route legal interpretation or contract approval decisions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/contract-comparison-free)
- [SkillPay purchase guidance referenced by the artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON summarizing clause comparison findings, missing input guidance, executed checks, and out-of-scope checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against user-provided contract text; insufficient input returns no conclusion.]

## Skill Version(s):

1.0.8 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

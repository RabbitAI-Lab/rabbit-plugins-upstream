## Description:

Conjecture Prover is a Chinese-language workflow that helps agents decompose conjectures, search for reductions or proof routes, validate intermediate claims, and produce clearly labeled proof or research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts can use this skill to structure conjecture work across mathematics, physics, computer science, biology, economics, linguistics, and history. It is best suited for planning reductions, organizing evidence, generating Markdown proof artifacts, and separating proven, verified, and still-open claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated conjecture analyses or proof drafts may be mistaken for authoritative mathematical, scientific, or historical conclusions.

Mitigation: Treat outputs as research scaffolding, preserve explicit proven/verified/open labels, and independently verify claims before relying on them.

Risk: The artifact includes an optional local verification script whose results could be overread as a complete proof.

Mitigation: Review the script before running it and interpret numerical checks as supporting evidence rather than conclusive proof.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/conjecture-prover)
- [Conjecture prover catalog](references/conjecture-prover-catalog.md)
- [Conjecture prover requirements](references/conjecture-prover-requirements.md)
- [Exemplars](references/exemplars.md)
- [RH proof verification script](scripts/rh_proof_verify.py)
- [RH artifact overview](assets/RH_README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown reports with optional code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proof status labels, reduction steps, validation checklists, and optional local verification scripts.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

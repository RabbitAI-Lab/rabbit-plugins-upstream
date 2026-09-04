## Description:

An advanced engineering skill for AI developers, cognitive science learners, and agent architects that explains how to implement agent memory systems, defend against memory poisoning, and quantify memory effectiveness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent engineers use this skill to design local agent memory systems, integrate memory tooling, run a six-dimension memory evaluation battery, and apply memory-poisoning defenses. It is also useful for technical learners who want cognitive-science evidence mapped to implementation choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The manual evaluation script can inspect local memory files and write a JSON report to the selected output path.

Mitigation: Run it only against memory folders intended for inspection and choose an explicit output path that is safe to overwrite.

Risk: The skill teaches memory-system patterns that may be implemented incorrectly or without enough review for memory-poisoning threats.

Mitigation: Use provenance tagging, untrusted-input gates, periodic audits, and human review before deploying memory behavior in production agents.

Risk: Included audit claims may not cover future changes or deployment-specific behavior.

Mitigation: Treat the audit as a release-time signal and rescan the skill before installation and after material edits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-brain-learning-memory-pro)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Research Sources and Evidence](references/调研出处与证据.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python examples, shell commands, configuration snippets, and optional JSON evaluation output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The evaluation script is manually run, uses the Python standard library, and writes a local JSON report when the user provides an output path.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter and manifest list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

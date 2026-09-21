## Description:

Verify a third-party ClawHub skill before installation by scanning its SKILL.md and scripts for contacted hosts, uploads, and credential-file reads, then reporting a clean, review, or suspicious verdict with file and line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeneassoft](https://clawhub.ai/user/aeneassoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and agents use this skill before installing untrusted ClawHub skills to identify declared network hosts, uploads, and credential-file reads. It helps decide whether a skill should be installed, reviewed further, or avoided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the clawphylax plugin for runtime monitoring and a local activity ledger.

Mitigation: Confirm the plugin is installed and enabled before relying on runtime monitoring, and review whether local activity logging is acceptable for the environment.

Risk: A clean scan only means nothing suspicious was found in the visible text.

Mitigation: Use the verdict as a pre-installation screen, review exact findings and source lines, and continue monitoring behavior after installation.

Risk: The scan reads files and cannot see what a downloaded script may do later.

Mitigation: Inspect referenced downloads and runtime behavior separately, especially when the skill fetches or executes external content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aeneassoft/skills/clawphylax-verify)
- [ClawPhylax project homepage](https://github.com/aeneassoft/clawphylax)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and verdict details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports clean, review, or suspicious verdicts with hosts, uploads, credential-read findings, and file and line evidence.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

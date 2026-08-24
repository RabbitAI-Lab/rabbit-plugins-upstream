## Description:

Text Utils provides local text-processing helpers for counting characters, Chinese characters, words, and lines; changing case; reversing text; deduplicating tokens; and trimming whitespace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and agents use this skill to run local text transformations and simple text measurements without sending text to a network service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may add python3 if it is missing.

Mitigation: Review and approve the package installation step according to local software policy before installing the skill.

Risk: Local text-processing output can be wrong for edge cases or unsuitable for decisions that require exact counts.

Mitigation: Review generated counts and transformations before using them in business-critical or compliance-sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/text-utils)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text and shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and may use python3 for mixed-language text counts.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

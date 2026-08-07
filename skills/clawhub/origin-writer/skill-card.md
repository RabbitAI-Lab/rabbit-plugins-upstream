## Description:

OriginWriter is a long-form novel writing workflow that turns each chapter into a semantic transaction with text and state changes, then validates continuity gates before persisting story state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and writing agents use OriginWriter to maintain long-form fiction continuity by submitting chapters as transactional text plus state changes, then checking world state, foreshadowing, assertions, and timeline consistency before persistence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install instructions use a placeholder repository, which could cause users to clone the wrong source.

Mitigation: Confirm the real repository behind the placeholder before installation and run the provided self-test first.

Risk: The workflow reads and writes the novel spec and package files supplied by the user.

Mitigation: Run it in a project workspace or version-controlled directory and review generated state changes before committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/origin-writer)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js 18 or newer and persists story state in user-selected novel spec/package files.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

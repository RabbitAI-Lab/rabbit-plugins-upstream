## Description:

Audits a repository for over-engineering and ranks opportunities to delete, simplify, or replace code with standard-library or native features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this read-only, repo-wide audit to prioritize unnecessary code, dependencies, and abstractions for possible removal or simplification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A full-repository audit may expose code structure in the agent conversation.

Mitigation: Run it only in conversations where sharing repository details is appropriate.

Risk: Simplification suggestions may overlook important uses or lead to unsuitable changes.

Mitigation: Review each proposal and check references before making changes; the skill itself does not edit files.

## Reference(s):

- [Project homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Numbered, ranked plain-text findings with tags, replacement suggestions, paths, and an estimated net reduction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recommendations; no files are changed. Reports 'Lean already. Ship.' if no cuts are found.]

## Skill Version(s):

4.13.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

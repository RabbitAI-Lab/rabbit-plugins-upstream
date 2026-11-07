## Description:

Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI Tools stakeholders use this skill to prepare a monthly digest from GitLab release and merge request evidence, with open work reported as a separate current snapshot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports partial scanner coverage because a local path-like reference could not be resolved.

Mitigation: Review the skill and its permissions in the host environment before installation, as the security guidance recommends.

Risk: The skill produces English-only digests and uses network and shell capabilities.

Mitigation: Confirm that the output language and required permissions fit the intended use before installation.

## Reference(s):

- [CI Tools project on GitLab](https://gitlab.com/xrow-public/ci-tools)
- [CI Tools Monthly Digest on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-digest)

## Skill Output:

**Output Type(s):** [Markdown]

**Output Format:** [English Markdown monthly digest with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers one complete UTC calendar month, with release and merged request counts, themes and migration notes; open requests are a separately dated snapshot.]

## Skill Version(s):

4.233.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

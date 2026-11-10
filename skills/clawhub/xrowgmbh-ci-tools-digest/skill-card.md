## Description:

Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work. Use for monthly reporting or an explicitly requested month.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI Tools maintainers use this skill to prepare an evidence-based monthly release digest, capture migration points, and track open work separately. It helps reviewers create and check the monthly report before proposing it through a merge request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial because a local path-like reference in SKILL.md could not be resolved, so its benign verdict has medium confidence.

Mitigation: Review the unresolved reference and skill contents before running it.

Risk: Collection uses GitLab network access and invokes the glab CLI through a subprocess, with GITLAB_TOKEN required.

Mitigation: Confirm the target project and token access before collection, and review the generated evidence and links before publishing.

Risk: The report is required to be English-only, which may omit nuance from source material in other languages.

Mitigation: Keep direct source links and verify translated claims against the original project material.

## Reference(s):

- [CI Tools project on GitLab](https://gitlab.com/xrow-public/ci-tools)
- [CI Tools Monthly Digest on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-digest)

## Skill Output:

**Output Type(s):** [Markdown, Files, Text]

**Output Format:** [English Markdown monthly digest with release and merge request evidence, migration notes, open work, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One complete UTC calendar month per report; open merge requests are shown as a separately dated snapshot.]

## Skill Version(s):

4.233.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

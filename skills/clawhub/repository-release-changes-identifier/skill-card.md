## Description:

Summarize repository changes for a release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release coordinators use this skill to turn a supplied repository patch into a concise release change set for handoff and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied commit patches may contain secrets or sensitive repository details.

Mitigation: Review patch text before use and avoid pasting credentials, tokens, or confidential details into the skill input.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/repository-release-changes-identifier)
- [Publisher Profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [JSON object with concise release change set fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces change_id, files, components, additions, and deletions from the supplied commit_patch text.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

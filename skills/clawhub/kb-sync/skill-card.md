## Description:

Knowledge base synchronization assistant for incrementally comparing and syncing local Markdown notes with cloud knowledge bases, with diff previews and conflict detection before changes are applied.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to preview incremental differences between a local note directory and a cloud knowledge base, then sync updates only after reviewing conflicts and planned changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-sync claims and destinations may be under-scoped for the user's actual knowledge base environment.

Mitigation: Use an explicit source directory and manifest path, run dry-run first, and verify the destination, token handling, and secret filtering before uploads or external API tools are used.

Risk: The learner module can persist usage and preference tracking data for arbitrary skill directories.

Mitigation: Remove or disable scripts/learner.py unless persistent usage and preference tracking is explicitly desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/kb-sync)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with shell command examples and local JSON manifest updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diff output lists planned additions, updates, and deletions; learner output may write usage and preference records.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps developers track prompt revisions, compare changes, and associate each version with an evaluation score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory: All rights reserved

## Use Case:

Developers and prompt teams use this skill to record differences between prompt files alongside evaluation scores, so they can review iterations and choose a version to reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local registry can contain sensitive text from prompt diffs.

Mitigation: Avoid processing prompts with secrets or sensitive customer data unless the registry file is handled appropriately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-version-control)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Local JSON version registry and text or JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry records version, score, timestamp, and added or removed prompt lines; documentation and theory are not covered by the code license.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

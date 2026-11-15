## Description:

Provides a reliable Tencent Docs write workflow for connector failures, long uploads, and post-write verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to diagnose failed Tencent Docs writes, retry or recover through the documented workflow, and verify the resulting document content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The evidence is incomplete because a referenced local path could not be resolved.

Mitigation: Review the unresolved reference before installation and verify that the referenced file is present and expected.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/haiyangchenbj/skills/tencent-docs-stable)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Procedural guidance and a concise verification report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long content is appended in paragraph-aligned chunks of at most 16 KB.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

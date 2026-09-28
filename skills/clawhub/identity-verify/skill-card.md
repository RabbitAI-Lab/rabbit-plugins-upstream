## Description:

Helps an agent identify the current conversation's login entry from a single authoritative configuration file and avoid confusing it with another account or entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All rights reserved

## Use Case:

People and agents use this skill to check which login entry belongs to the current conversation, ask the user when it cannot be confirmed, and apply the correct entry label in replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests writing and web search permissions beyond its stated read-only identity check.

Mitigation: Review before installation; prefer read/search access limited to the specific authoritative local configuration file.

Risk: Broad activation wording may trigger identity checks when they were not requested.

Mitigation: Use narrower, opt-in identity-check trigger phrases.

## Reference(s):

- [Identity Verify release on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/identity-verify)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies the entry when evidence is sufficient; otherwise asks the user to confirm.]

## Skill Version(s):

1.0.2 (source: ClawHub release; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

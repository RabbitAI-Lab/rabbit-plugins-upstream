## Description:

Prepare, sanitize, publish, and verify public GitHub issues, pull requests, review comments, release notes, bug reports, logs, screenshots, and test evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jumpunder](https://clawhub.ai/user/jumpunder)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn private incident context into sanitized public GitHub contributions and to verify drafts, metadata, attachments, and fetched public results before or after publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A public GitHub write could expose private context, credentials, attachments, or the wrong publishing identity.

Mitigation: Require explicit authorization and review the exact draft, destination, identity, attachments, and fetched public result before treating the release as safe.

Risk: The deterministic scanner can miss sensitive disclosures that are not covered by configured patterns or deny terms.

Mitigation: Keep deny-term files private, audit prose, code, metadata, logs, images, attachments, and links, and read the final draft as a public artifact after the scanner passes.

Risk: Exposed public information may remain in notifications, forks, caches, clones, or third-party indexes even after edits or deletion.

Mitigation: Stop further publication, remove or replace the exposed artifact with authorization, rotate exposed credentials, rescan the replacement, and state what cannot be recalled.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user authorization before external GitHub writes and treats a passing preflight scan as necessary but not decisive.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Converts public AI chat share links and local conversation histories into Markdown while preserving tables, code blocks, and message timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mapleleo-hub](https://clawhub.ai/user/mapleleo-hub)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can archive public AI chat links, search or export local conversation history, and bring prior conversation context into a current session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the skill suspicious because it relies on an unpinned executable dependency, and analysis of most bundled files was incomplete.

Mitigation: Treat this as a review-needed skill; consider avoiding installation until the dependency is pinned to a reviewed version and the incomplete file analysis is resolved. If installed, account for the possibility that the external dependency could run with your account’s privileges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mapleleo-hub/skills/chat-share-reader)
- [Local session sources](references/sessions.md)
- [Supported share sites](references/sites.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Text]

**Output Format:** [Markdown conversation archives, with optional JSON or plain text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversation exports can be saved as files or printed to stdout; local session exports can include full conversation data.]

## Skill Version(s):

0.1.0 (source: release evidence, package.json, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Looks up IETF RFCs, checks whether specifications are current or obsolete, and retrieves focused sections for standards-grounded answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, standards reviewers, and agents use this skill to find RFCs, verify supersession status, inspect section headings, and quote relevant specification text instead of relying on memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional full-corpus sync downloads about 512 MB of public RFC text from an unauthenticated rsync source.

Mitigation: Use normal on-demand HTTPS lookup commands for most work; run sync only when explicitly requested, and independently verify synced text for high-assurance standards work.

## Reference(s):

- [RFC Editor Index](https://www.rfc-editor.org/rfc-index.txt)
- [RFC Editor RFC text endpoint](https://www.rfc-editor.org/rfc/rfc{number}.txt)
- [Release changelog](https://github.com/shbernal/rfc-ai-tooling/releases/tag/v0.4.0)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May fetch RFC text over HTTPS on demand; optional local full-text sync is explicitly user-controlled.]

## Skill Version(s):

0.4.0 (source: release evidence and script __version__)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

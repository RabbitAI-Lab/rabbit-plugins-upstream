## Description:

Helps developers test regular expressions, inspect matches and capture groups, and preview substitutions against supplied text or file contents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory: all rights reserved

## Use Case:

Developers and other agent users can quickly check regex matches, captured groups, flags, and replacement previews without changing their application code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions claim apply, backup, text-replace, and duplicate-finding features that the bundled regex tester does not provide.

Mitigation: Use this release only to test expressions and preview substitutions; do not rely on the claimed write or backup features.

Risk: The requested Write and WebFetch permissions exceed what regex testing needs.

Mitigation: Do not grant Write or WebFetch unless a later release documents and limits their use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/regex-sandbox)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON with match counts, spans, captured groups, and optional replacement preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns exit status 0 when matches are found, 1 when none are found, and 2 for invalid patterns or arguments.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

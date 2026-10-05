## Description:

Helps agents test regular expressions against text or files, inspect matches and capture groups, and preview replacements in plain text or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and other agents can quickly test regex patterns, flags, capture groups, and replacement results without editing the input file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests write, shell, and web access beyond what the visible regex helper needs.

Mitigation: Review before installation; restrict unnecessary tools and require explicit confirmation before any file-changing action.

Risk: Documentation mentions applying changes, but the visible helper only previews replacements.

Mitigation: Do not rely on a claimed apply or backup workflow; back up important files and inspect outputs before making changes separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/regex-sandbox)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON containing matches, capture groups, and optional replacement preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes: 0 for matches, 1 for no matches, 2 for invalid patterns or arguments; the helper does not write input files.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release; artifact version labels differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

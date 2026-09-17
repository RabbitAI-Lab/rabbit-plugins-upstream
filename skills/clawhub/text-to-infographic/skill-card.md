## Description:

Organizes user-supplied conversation content into a single-page infographic specification and, when explicitly requested, copyable standalone static HTML source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn content already provided in the current conversation into a one-page infographic plan, or into copyable static HTML source when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be prompted to invent missing facts, numbers, citations, or assets for an infographic.

Mitigation: Keep missing items unspecified and trace display claims to content the user already provided in the current conversation.

Risk: Users may request browsing, local file reads, code execution, saved files, rendering, or publishing beyond the skill boundary.

Mitigation: Do not browse, read local files, run commands, save files, render PNG or PDF outputs, or publish; ask the user to paste needed source content into the conversation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/text-to-infographic)
- [Text to Infographic README](artifact/README.md)
- [FAQ](artifact/docs/faq.md)
- [Canonical cases](artifact/docs/canonical-cases.md)
- [GEO evaluation](artifact/docs/geo-evaluation.md)
- [GEO manifest](artifact/geo-manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown text; optionally a single complete static HTML code block.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only current-conversation content; HTML output is one page, self-contained, static, inline CSS only, and has no external dependencies.]

## Skill Version(s):

1.1.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

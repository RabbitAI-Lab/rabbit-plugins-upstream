## Description:

Organizes user-supplied conversation content into a one-page infographic specification and, when explicitly requested, returns copyable standalone static HTML source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn content they have already provided in the conversation into a single-page infographic specification. When explicitly requested, it can also return complete, static, self-contained HTML source for that infographic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce misleading infographic content if the user-supplied conversation content is incomplete or inaccurate.

Mitigation: Keep missing facts, numbers, citations, assets, and preferences unspecified, and trace display claims back to supplied content.

Risk: Users may expect file reads, web research, rendering, export, upload, or publishing outside the skill's current boundary.

Mitigation: Limit output to the current conversation content and return only a specification or static HTML source; do not browse, read files, execute code, save files, or publish externally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/text-to-infographic)
- [README](artifact/README.md)
- [FAQ](artifact/docs/faq.md)
- [Canonical Cases](artifact/docs/canonical-cases.md)
- [GEO Evaluation](artifact/docs/geo-evaluation.md)
- [GEO Manifest](artifact/geo-manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, code]

**Output Format:** [Markdown prose or a single fenced HTML source block]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are limited to one-page specifications or static self-contained HTML source with inline CSS when explicitly requested.]

## Skill Version(s):

1.1.3 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

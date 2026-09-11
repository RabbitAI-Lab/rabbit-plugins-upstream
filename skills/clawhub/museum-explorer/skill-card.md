## Description:

museum-explorer helps users plan museum and gallery visits, verify exhibition facts, guide on-site viewing, and produce post-visit journals with SVG stamp collections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to prepare for museum or gallery visits, get on-site exhibit guidance, and turn completed visits into reusable journals, checklists, and stamp collections. The workflow is most useful when exhibition details need source dates, cross-checks, and clear uncertainty labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML journals can make under-disclosed outbound web requests to jsDelivr for a font.

Mitigation: Review generated journals before installation or sharing, and prefer disabling the remote font or bundling it locally.

Risk: The journal template currently relies on the agent to keep photo paths local.

Mitigation: Use local relative photo paths only, validate paths before rendering journals, and add a restrictive Content Security Policy before using journals with personal photos.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/museum-explorer)
- [source-verification.md](references/source-verification.md)
- [data-sources.md](references/data-sources.md)
- [exhibits.schema.json](references/exhibits.schema.json)
- [stamp-design-guide.md](references/stamp-design-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, HTML, JSON, and SVG files with explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local session files, exhibition data, journal HTML, and SVG stamps under the documented workspace paths after user-facing confirmation.]

## Skill Version(s):

1.6.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Reconstructs an open-source project's growth channels, key content, and stage-by-stage attribution from GitHub history and public web evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gingiris-1031](https://clawhub.ai/user/gingiris-1031)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, maintainers, and growth teams use this skill to investigate open-source project star growth and produce an evidence-backed attribution report across GitHub, launch channels, social platforms, and technical content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may ask an agent to browse public web sources and call the GitHub API, which can expose unnecessary token permissions if a broad token is supplied.

Mitigation: Use the least-privileged GitHub token suitable for public read-only API access and avoid providing private repository credentials unless required.

Risk: Attribution conclusions can be misleading when public signals are incomplete or when platform effects overlap.

Mitigation: Report uncertainty, use ranges instead of precise percentages, keep unsupported hypotheses separate, and label modeled or inferred claims explicitly.

## Reference(s):

- [API Playbook](artifact/references/api-playbook.md)
- [Attribution Model](artifact/references/attribution-model.md)
- [Evidence Schema](artifact/references/evidence-schema.md)
- [ClawHub Skill Page](https://clawhub.ai/gingiris-1031/skills/oss-growth-attribution)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with tables, source URLs, modeled attribution ranges, and recommended instrumentation steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Material claims should include a URL or be clearly labeled as modeled, inferred, or unsupported.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

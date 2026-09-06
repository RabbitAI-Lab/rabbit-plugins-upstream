## Description:

Offline website mirroring with HTTrack: snapshot one page with its assets or mirror a bounded site to disk for offline reading, backup, or research using scripted recipes, polite defaults, strict URL validation, resumable mirrors, and stable JSON reports for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to create authorized offline snapshots or bounded website mirrors with HTTrack while receiving machine-readable status and result reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-looking URLs can still cause crawler access to internal services through DNS or redirects.

Mitigation: Run the skill only from environments where broad outbound crawling is acceptable, and avoid untrusted URLs when the machine can reach cloud metadata, admin panels, or intranet services.

Risk: Mirrored files and log output may contain untrusted content.

Mitigation: Review mirrored files and log_tail content before opening, processing, or sharing them.

Risk: Mirroring content may violate site terms, copyright, or operational expectations.

Mitigation: Mirror only sites you are authorized to archive, honor robots settings, and keep crawls bounded with depth, socket, time, and size limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/httrack)
- [Recipes](artifact/docs/recipes.md)
- [Flag evidence](artifact/docs/evidence.md)
- [Machine manifest](artifact/manifest.json)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON report contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces httrack.doctor.v1 and httrack.report.v1 JSON reports for machine consumption.]

## Skill Version(s):

2.0.1 (source: server release metadata, SKILL.md frontmatter, manifest.json, README.md, and CHANGELOG.md released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

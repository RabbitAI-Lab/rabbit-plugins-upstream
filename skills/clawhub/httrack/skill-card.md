## Description:

Offline website mirroring and web archiving with HTTrack. Mirror a website to local disk for offline browsing, backup, or research, with recipes for depth-limited crawls, single-page snapshots, and incremental mirror updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, archivists, and other external users can use this skill to mirror authorized websites or pages for offline browsing, backup, evidence capture, and local corpus creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mirroring sites without authorization can violate site terms, copyright, or access expectations.

Mitigation: Mirror only sites you are authorized to archive, respect robots.txt and site terms, and avoid redistributing mirrored content without permission.

Risk: Large or aggressive crawls can put unwanted load on target servers.

Mitigation: Keep crawl depth and connection count modest; the included wrapper uses robots.txt and two parallel connections by default.

Risk: Downloaded mirrors can contain active scripts, cookies, tracking pixels, or unexpected pages.

Mitigation: Review mirrored files before opening, sharing, or using them as evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/httrack)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash commands and a shell wrapper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local website mirror files in the user-specified output directory when the included wrapper or HTTrack commands are run.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

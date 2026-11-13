## Description:

Audits one public website for answer-engine crawlability, readability, and quotability, then produces a prioritized fix list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aureliusclaw](https://clawhub.ai/user/aureliusclaw)

### License/Terms of Use:

MIT

## Use Case:

Developers, site owners, and technical SEO teams use Geo Scan to assess whether answer engines can crawl, interpret, and quote a public site, then prioritize technical improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is incomplete (9 of 10 components scanned) and identifies request-pacing and scan time-limit weaknesses.

Mitigation: Before installing, decide whether these weaknesses are acceptable for the intended use; review request scheduling and whether one deadline across network operations is needed.

## Reference(s):

- [Geo Scan release on ClawHub](https://clawhub.ai/aureliusclaw/skills/geo-scan)
- [Project information listed in the skill metadata](https://github.com/AureliusClaw/geo-scan)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [A scored website audit with evidence, a prioritized fix list, and per-page findings, as Markdown or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One automated sample of up to 25 pages; scores include the evidence used for each finding.]

## Skill Version(s):

1.2.6 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

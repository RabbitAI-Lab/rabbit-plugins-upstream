## Description:

Cite Holmes conducts evidence-calibrated literature research, verifies citation records against scholarly registries, and produces research reports and bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use the skill to discover literature, check whether references are authentic and relevant, review evidence and retraction status, and prepare citation-focused reports and bibliography exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation-verification guarantees and network safeguards have confirmed gaps.

Mitigation: Use a reviewed, pinned revision with restricted network access, and independently check important citations and retraction status.

Risk: URL-based Semantic Scholar authentication may expose a supplied API key.

Mitigation: Do not supply a Semantic Scholar key until URL-based authentication is removed.

Risk: Offline mode may still use networked model endpoints, and cache controls do not fix verification gaps.

Mitigation: Do not rely on offline mode when model endpoints are configured; disabling disk caching and using one worker only reduces confirmed cache-reuse paths.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification Details](references/verification-details.md)
- [Medical Mode](references/medical-mode.md)
- [Report Template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, BibTeX, RIS]

**Output Format:** [Research and citation-verification reports, plus bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include per-reference verification outcomes; unverified or unreachable references should remain clearly distinguished from verified references.]

## Skill Version(s):

4.7.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

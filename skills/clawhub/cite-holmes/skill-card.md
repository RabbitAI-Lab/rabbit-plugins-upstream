## Description:

Guides deep research and checks citations against source material and scholarly registries before presenting a sourced report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check bibliographies and in-text citations, and prepare reports that distinguish verified sources from references needing human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference checking makes outbound requests and may disclose submitted reference data.

Mitigation: Review reference data and network access before use; do not submit sensitive material to untrusted endpoints.

Risk: Untrusted reference URLs could be used to probe internal network services.

Mitigation: Avoid untrusted URLs in privileged networks and restrict the verifier's network access.

Risk: An exposed MCP HTTP/SSE server could accept requests from untrusted callers.

Mitigation: Keep the server private and accessible only to trusted callers.

Risk: External judging endpoints may receive sensitive drafts; an always-current install path can differ from the reviewed release.

Mitigation: Use only trusted judging endpoints for sensitive work and prefer the reviewed ClawHub artifact when release provenance matters.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](artifact/references/verification-details.md)
- [Security and behavior](artifact/references/security.md)
- [Report template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Sourced research and citation-verification reports in Markdown, with a JSON workpaper and optional bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-reference verdicts, evidence grades, human-review flags, and optional BibTeX, RIS, GB/T 7714, or CSV exports.]

## Skill Version(s):

4.2.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

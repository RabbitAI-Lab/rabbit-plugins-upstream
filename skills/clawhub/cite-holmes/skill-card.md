## Description:

Guides source-backed research and checks bibliography entries against citation registries before presenting a report or citation audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions with source citations or check a bibliography for invalid, mismatched, and retracted references. It separates uncertain entries for human review rather than treating every reachable source as verified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation identifiers, titles, and reference URLs may be sent to external services during verification.

Mitigation: Use --offline for sensitive bibliographies, and --no-cache to avoid retaining local verdicts.

Risk: Following untrusted reference URLs or redirects may reach internal services.

Mitigation: Avoid untrusted URLs and run arbitrary URL checks in a sandboxed, network-restricted environment.

Risk: Optional judge or NLI endpoints may receive claim and evidence text.

Mitigation: Only set --judge-url or --nli-url to endpoints you trust with that text.

## Reference(s):

- [Cite Holmes ClawHub listing](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Citation verification details](references/verification-details.md)
- [Research report template](references/report-template.md)
- [Medical evidence mode](references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON, BibTeX, CSV, Guidance]

**Output Format:** [Source-cited research report or citation audit, with optional structured audit and bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation verdicts distinguish verified, partial, unverified, unreachable, and invalid entries; uncertain findings require human review.]

## Skill Version(s):

3.4.0 (source: server-resolved release; bundled frontmatter says 3.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps researchers investigate questions and check citations against source and registry evidence before including them in a report or bibliography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to research questions, check bibliographies and in-text citations, and produce reports that distinguish verified, incomplete, unreachable, and unverified sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking attacker-supplied citation URLs may reach internal web services.

Mitigation: Review before installation; avoid untrusted citation URLs and run URL checks with restricted network access.

Risk: External judging endpoints can receive document and claim text.

Mitigation: Use --judge-url, --nli-url, and --fast-judge-url only with local or otherwise trusted endpoints for sensitive material.

Risk: The default local verdict cache can persist sensitive bibliography data.

Mitigation: Use --no-cache when checking sensitive bibliographies.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Reference index](artifact/references/INDEX.md)
- [Verification details](artifact/references/verification-details.md)
- [Medical evidence mode](artifact/references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSON, Shell commands]

**Output Format:** [Research reports and citation-verification summaries in Markdown or text; optional JSON workpapers and bibliography exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation verdicts and evidence grades include flags for human review; optional BibTeX, RIS, CSV, and GB/T 7714 exports.]

## Skill Version(s):

3.13.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

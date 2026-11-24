## Description:

Rewrites an Amazon US listing from a spec sheet, checks the title and bullet limits, and flags the claim words Amazon restricts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

For Amazon US sellers and brand managers preparing product listings. The bundled checker reports missing title and bullet sections, lines over 200 characters, and a small set of flagged phrases; review its report because the available security assessment says the checker does not provide the advertised rewrite.

### Deployment Geography for Use:

United States (Amazon US)

## Known Risks and Mitigations:

Risk: The available security assessment says the bundled checker lints existing text and does not provide the advertised listing rewrite, so relying on it alone may leave the listing unfinished.

Mitigation: Draft or review the listing separately, and treat the checker report as a limited aid rather than a completed rewrite.

Risk: The checker writes a report to an output directory without a declared tool scope.

Mitigation: Run it with an output directory you control and inspect the report before using it.

## Reference(s):

- [Amazon US listing rules (bundled reference)](references/amazon-listing-rules.md)
- [ClawHub skill release](https://clawhub.ai/rapidworker1/skills/amazon-listing-optimizer)
- [Publisher profile](https://clawhub.ai/user/rapidworker1)
- [Publisher homepage (metadata link)](https://github.com/rapidworker1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Listing copy guidance and a Markdown lint report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill describes a title, five bullets, search terms, and claim flags; the bundled checker writes a report identifying missing sections, long lines, and selected phrases.]

## Skill Version(s):

1.0.7 (source: skill frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

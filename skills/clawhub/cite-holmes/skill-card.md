## Description:

Guides deep research and checks cited references against academic registries before presenting evidence-graded conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check bibliographies and draft citations, and prepare research reports that distinguish verified evidence from references needing human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Networked citation checks may access untrusted reference URLs and external services.

Mitigation: Do not check untrusted URLs on sensitive networks; review the ClawHub package before running it.

Risk: The live GitHub installation command can retrieve code that differs from the reviewed release.

Mitigation: Prefer the reviewed ClawHub package over the live GitHub installation command.

Risk: Exposing the optional MCP HTTP server beyond the local machine broadens access.

Mitigation: Keep MCP HTTP mode bound to localhost.

Risk: Optional external judging endpoints may receive citation content.

Mitigation: Use external judging endpoints only when you control and trust them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](artifact/references/verification-details.md)
- [Security and behavior declaration](artifact/references/security.md)
- [Limitations and exclusions](artifact/references/out-of-scope.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown research reports and citation-check results, with optional structured exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes citation verdicts, evidence grades, and items requiring human review.]

## Skill Version(s):

3.14.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

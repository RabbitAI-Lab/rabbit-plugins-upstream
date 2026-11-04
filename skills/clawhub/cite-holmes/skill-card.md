## Description:

Cite Holmes searches scholarly literature, verifies citations against registries, and creates research reports and bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Researchers, analysts, and developers can use the skill to discover literature, investigate questions, check whether cited sources and identifiers resolve, and prepare reviewable research reports or bibliography files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted citation links can bypass network safeguards.

Mitigation: Block private destinations before processing untrusted citation links.

Risk: Incomplete checks can produce misleading verification results.

Mitigation: Follow human-review flags and independently confirm verified references and retraction status, especially for medical work.

Risk: Online checks disclose citation identifiers, titles, and submitted URLs to external services.

Mitigation: Use online checks only when that disclosure is acceptable.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Security and behavior](references/security.md)
- [Verification details](references/verification-details.md)
- [Medical mode guidance](references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, JSON workpapers, Bibliography exports (BibTeX, RIS, CSV, GB/T 7714)]

**Output Format:** [Markdown and JSON, with optional bibliography export formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation results include verification verdicts and may flag unresolved checks for human review.]

## Skill Version(s):

6.0.0 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

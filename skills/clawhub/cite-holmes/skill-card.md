## Description:

Cite Holmes conducts scoped literature research and verifies citations against academic registries before producing sourced reports and bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and authors use the skill to investigate questions, verify citation authenticity and retraction status, and prepare evidence-graded reports or bibliography exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation links may reach private-network services.

Mitigation: Use a reviewed, fixed release in an environment that blocks private-network access.

Risk: Offline mode may still transmit data when optional model endpoints are configured.

Mitigation: For confidential material, enforce network blocking externally; do not rely on offline mode alone.

Risk: Verification results may overstate certainty.

Mitigation: Independently check important citations and retraction status; disable caching and use one worker when comparing conflicting references.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Security and behavior declaration](references/security.md)
- [Verification details](references/verification-details.md)
- [Scope and limitations](references/out-of-scope.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Bibliography files]

**Output Format:** [Markdown research reports, JSON workpapers, and BibTeX, GB/T 7714-2025, RIS, or CSV bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [References carry explicit verification verdicts; unchecked and unreachable items remain identified as such.]

## Skill Version(s):

4.8.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

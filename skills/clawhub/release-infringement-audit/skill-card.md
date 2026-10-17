## Description:

Screens projects before release for license, third-party code, asset, trademark, and exposed-secret risks, then produces a prioritized report with evidence and suggested actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[y16689540962-cloud](https://clawhub.ai/user/y16689540962-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill to screen projects before publishing to npm, ClawHub, or GitHub and review prioritized findings before release. Its automated findings are not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit automatically executes a check-secrets.sh script from the repository being reviewed.

Mitigation: Review the skill and audit only trusted repositories; otherwise disable that delegation or run the audit in a sandbox without credentials or network access.

Risk: The audit may contact the npm registry when local dependency metadata is unavailable.

Mitigation: Run without network access when external lookups are inappropriate, and verify incomplete dependency findings manually.

## Reference(s):

- [Release Infringement Audit on ClawHub](https://clawhub.ai/y16689540962-cloud/skills/release-infringement-audit)
- [Verdict basis](references/verdict-basis.md)
- [SPDX License List](https://spdx.org/licenses/)
- [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html)
- [Creative Commons FAQ on software licensing](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Prioritized Markdown or JSON audit report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, evidence, rationale, and recommended action; the report is an automated screening, not legal advice.]

## Skill Version(s):

1.0.1 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

IPQualityScore helps agents use OOMOL's oo CLI to check IP reputation, scan URLs or domains, and validate email addresses or phone numbers through a connected IPQualityScore account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run IPQualityScore reputation, URL safety, email validation, and phone validation checks from an agent through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could execute unreviewed shell or PowerShell content.

Mitigation: Inspect and verify the official installer path before use, and require explicit approval before installing or updating the oo CLI.

Risk: IPQualityScore access is mediated through OOMOL-connected credentials.

Mitigation: Use the skill only when the user accepts OOMOL-mediated access and has intentionally connected the relevant IPQualityScore account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ipqualityscore)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [IPQualityScore homepage](https://www.ipqualityscore.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; normal action responses include data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

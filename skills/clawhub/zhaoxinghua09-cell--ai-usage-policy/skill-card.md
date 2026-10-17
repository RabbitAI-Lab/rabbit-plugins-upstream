## Description:

Generates a one-page team AI usage policy covering approved tools, permitted uses, prohibited uses, and incident escalation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Team leads and governance staff use this skill to draft a concise AI-use policy for onboarding, approved-tool changes, incident response, or audit preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation examples use outdated command-line options, which may lead to an incomplete or failed policy draft.

Mitigation: Check the script's --help output for current options and review the generated policy before distribution.

Risk: Broader agent permissions than the local generator needs could expose sensitive policy inputs or enable unintended file changes.

Mitigation: Limit access to necessary inputs and output paths; avoid WebFetch and broad write permissions unless the hosting platform requires them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-usage-policy)
- [LGD theory reference (linked in README)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSON]

**Output Format:** [One-page Markdown policy printed to stdout or written to a file; optional JSON response containing the policy text and output path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The policy includes a generation date and the supplied escalation contact; approved tools and prohibited uses are customizable.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; bundled documentation says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

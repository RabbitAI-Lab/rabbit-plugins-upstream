## Description:

Analyzes Shopee brand trends by month, quarter, or year across multiple regional sites for up to 720 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to compare long-term brand performance across supported regional sites and identify monthly, quarterly, or annual trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or updating of local tooling and shell profile changes can alter the user's environment.

Mitigation: Use a trusted, pinned, user-approved qhkit installation; avoid automatic global installs, unpinned npx execution, and profile changes.

Risk: The skill requires a locally configured Qinghu API token.

Mitigation: Have the user configure the token through an approved credential workflow and avoid exposing it in shared output.

Risk: Trend queries can consume paid Qinghu credits.

Mitigation: Estimate charges and obtain the user's consent before making paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown analysis and optional tabular files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multi-site comparisons and up to 720 days of trends; paid data calls require user approval.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

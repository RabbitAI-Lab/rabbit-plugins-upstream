## Description:

Use when the user wants a concise daily or weekly site/growth standup from TrustGrowth history when connected or from validated available evidence and repository artifacts otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and site owners use this skill to produce concise daily or weekly site and growth standups from TrustGrowth history, validated evidence, or repository and audit artifacts. It is intended for internal situational updates, not client-facing score reports or deep-dive audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release scanner marked the skill suspicious because it requires running an unbundled validator script from the active skills root.

Mitigation: Install only when the Groundcrew skills root is trusted and the referenced groundcrew-doctor.py script can be verified before use.

Risk: Connected SEO and analytics providers may expose site and business data.

Mitigation: Prefer read-only credentials, do not print secrets, and confirm paid connectors before use.

Risk: A standup can become misleading if it implies historical movement without comparable persisted observations.

Mitigation: Report unavailable measurements as unknown, preserve nulls, and say no comparable baseline when a measured delta is not available.

## Reference(s):

- [Connectors and Categories](references/connectors.md)
- [Reporting Contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)
- [ClawHub Skill Page](https://clawhub.ai/trustgrowth/skills/standup)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown standup summary with concise sections and optional inline command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps each site to about 15 lines, labels missing baselines plainly, and recommends at most one missing connector.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

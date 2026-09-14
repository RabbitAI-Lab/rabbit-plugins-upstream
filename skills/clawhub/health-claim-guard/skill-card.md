## Description:

Health Claim Guard screens health-product and food marketing copy for prohibited therapeutic claims and required warning language, returning deterministic pass/fail results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and compliance reviewers use this skill to pre-screen health-related promotional copy for prohibited disease-treatment or absolute claims and missing warning text. It is an initial compliance aid and does not replace official regulatory guidance or licensed professional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned global installation can fetch mutable remote code and make global agent-skill changes.

Mitigation: Run the bundled Python script directly or install only from a pinned, reviewed commit or package version.

Risk: The scanner provides preliminary compliance findings and may miss context-specific legal or medical requirements.

Mitigation: Use results as an initial screen, then verify against official current rules and qualified professional guidance before regulated or high-impact use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/health-claim-guard)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [README](README.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text pass/fail findings or JSON results, with optional shell command usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Return codes indicate pass, fail, or usage error; findings are preliminary compliance screening and require human review for regulated decisions.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact SKILL.md frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

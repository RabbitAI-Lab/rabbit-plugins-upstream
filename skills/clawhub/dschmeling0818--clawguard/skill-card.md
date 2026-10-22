## Description:

ClawGuard assesses third-party OpenClaw and AgentSkills bundles before use and returns a free verdict or an optional paid detailed scan report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dschmeling0818](https://clawhub.ai/user/dschmeling0818)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use ClawGuard to assess third-party skills before installing, executing, or trusting them. The free preview provides a verdict; the optional paid scan returns a detailed report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning may upload secrets or files outside the selected skill folder to the hosted service.

Mitigation: Enforce symlink containment and exclude sensitive files, or scan an isolated copy containing only approved files. Treat the service's retention claims as unverified.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dschmeling0818/skills/clawguard)
- [ClawGuard service](https://clawguard.duckdns.org:8082)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text CLI verdict and scan report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports a verdict, risk score, file counts, and findings; the full scan report is an optional paid service.]

## Skill Version(s):

1.0.1 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Security advisory feed package for OpenClaw-related threats and vulnerabilities. The upstream feed is updated daily; local automation is handled by clawsec-suite or the operator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[davida-ps](https://clawhub.ai/user/davida-ps)

### License/Terms of Use:

AGPL-3.0-or-later

## Use Case:

Developers and operators use ClawSec Feed to review OpenClaw-related security advisories and cross-reference them with installed skills or their own polling workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Standalone install and update instructions can trust mutable remote files enough to replace the installed skill.

Mitigation: Use a pinned release and signed-manifest verification before installing or updating, especially on production hosts.

Risk: Advisory feed text is untrusted data and may describe actions such as removals, file changes, or disclosures.

Mitigation: Require explicit user confirmation before converting advisory content into commands, file changes, removals, or disclosures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/davida-ps/skills/clawsec-feed)
- [ClawSec homepage](https://clawsec.prompt.security)
- [ClawSec feed release metadata](https://api.github.com/repos/prompt-security/ClawSec/releases?skill=clawsec-feed)
- [ClawSec advisory feed](https://raw.githubusercontent.com/prompt-security/ClawSec/main/advisories/feed.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON advisory feed data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory feed content should be treated as untrusted data and reviewed before acting.]

## Skill Version(s):

0.0.11 (source: frontmatter, skill.json, changelog, release metadata; released 2026-06-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

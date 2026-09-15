## Description:

Scrapingdog helps an agent fetch web pages and retrieve parsed Scrapingdog results for Google Search, Google Scholar, Google Maps search, Google Maps place lookup, and account usage requests through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Scrapingdog read and search actions from an agent after their OOMOL account and Scrapingdog connection are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute code on the user's machine.

Mitigation: Review setup instructions before installation, prefer verified signed or package-manager sources for the oo CLI, and run remote installer commands only when the OOMOL distribution channel is trusted.

## Reference(s):

- [ClawHub Scrapingdog Skill](https://clawhub.ai/oomol/skills/oo-scrapingdog)
- [Scrapingdog Homepage](https://www.scrapingdog.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routine actions return connector JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Yotta-triage is a zero-dependency static malware triage skill that hashes files, identifies file types, measures entropy, extracts classified strings, parses PE and ELF headers, and produces triage reports plus IOC lists without executing samples or using the network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts, incident responders, developers, and agent users use this skill to perform authorized, local-first static triage of suspicious files or sample directories before deeper manual, sandbox, or intelligence review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can overwrite an existing yotta-triage skill directory or install the skill across many agent directories without an interactive confirmation step.

Mitigation: Review installer behavior before use, prefer a single explicit skills directory with --dir, avoid -g unless broad installation is intended, and check for an existing yotta-triage directory before copying.

Risk: Static malware triage results are suspicious indicators, not definitive malicious verdicts.

Mitigation: Use the skill only on authorized samples, keep analysis local and offline, and confirm conclusions with human review, sandboxing, or trusted threat-intelligence sources.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-triage)
- [Static triage specification](references/triage-spec.md)
- [Risk scoring model](references/risk-model.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-triage)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Text reports, Markdown reports, JSON reports, or IOC-only JSON arrays]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline, read-only static analysis; IOC records cover hashes, URLs, domains, IPv4 addresses, and email addresses.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

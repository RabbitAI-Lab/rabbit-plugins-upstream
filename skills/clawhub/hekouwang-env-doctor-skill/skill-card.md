## Description:

Scans macOS and Linux developer environments for disk usage from development tools, classifies findings as data, cache, or leftover, and guides the user through read-only reporting plus opt-in cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect local development-environment disk usage, identify obsolete version managers or large caches, and decide what can be cleaned without losing important data. It is especially useful for macOS and Linux machines with Node, Python, container, Xcode, package-manager, or AI-agent caches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cleanup selector can delete selected cache or leftover tool directories.

Mitigation: Start with the read-only scan or clean.sh --dry-run, review each listed item and cost, and execute cleanup only after explicit confirmation.

Risk: Scan output can reveal local development-environment metadata such as cache sizes, shell config markers, runtime locations, and agent-host directory sizes.

Mitigation: Keep scan reports local unless sharing is necessary, and review reports before sending them outside the machine or organization.

Risk: An active tool could be disrupted if conflicting signals are treated as a confident leftover finding.

Mitigation: Use the four-signal classification rules, mark contradictions as uncertain, and avoid deleting data-class entries or active version-manager directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-env-doctor-skill)
- [Project homepage](https://github.com/huiyonghkw/hekouwang-env-doctor-skill)
- [Safety rules](references/safety.md)
- [Classification rules](references/rules.md)
- [Report workflow](references/report.md)
- [Doctor suite](references/doctor-suite.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with inline bash commands and plain-text scan output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are grouped as leftover, cache, data, or uncertain; cleanup is opt-in through a dry-run-capable selector with confirmation.]

## Skill Version(s):

1.2.1 (source: frontmatter, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

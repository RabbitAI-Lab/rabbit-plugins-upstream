## Description:

Conclave is a multi-agent reasoning skill that orchestrates multiple AI CLIs into structured debates where agents independently analyze a problem, challenge competing arguments, identify flaws, and refine reasoning across rounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mclyang](https://clawhub.ai/user/mclyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and decision makers use Conclave to convene multiple AI agents for structured debate, cross-examination, convergence, and a chair-adjudicated final report. It is intended for consequential decisions such as architecture choices, contract risk, pricing, and investment analysis rather than simple trivia.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update global CLI tools and may invoke package managers or sudo-capable system package installers.

Mitigation: Run install.sh with --check-only first, prefer preflight.sh --skip-update when updates are not needed, and review any npm, brew, apt, dnf, pacman, winget, or sudo action before allowing it.

Risk: Debate prompts, final drafts, and round summaries may be sent to multiple third-party AI providers and the Manus API.

Mitigation: Avoid regulated, proprietary, classified, or sensitive personal data unless provider data policies and consent requirements have been reviewed.

Risk: Full debate records are retained under ~/.hermes/debates/ and exported into the current working directory.

Mitigation: Run debates from an isolated non-synced workspace and use cleanup.sh or manual deletion to control retention.

Risk: Credential and authentication readiness checks depend on local files, shell environment variables, OAuth state, and external service availability.

Mitigation: Complete every install.sh ACTION item, run preflight.sh before each debate, and stop until failed provider pings are fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mclyang/skills/conclave-skill)
- [Conclave Consensus Protocol v1.1](artifact/references/consensus-protocol-v1.md)
- [Panelist Roster](artifact/references/panelists.md)
- [Manus Tasks API](https://api.manus.im/v1/tasks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown reports, debate archives, inline shell commands, and configuration checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates persistent debate folders under ~/.hermes/debates/ and can export final reports, minutes, indexes, preflight logs, and calibration records.]

## Skill Version(s):

1.6.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

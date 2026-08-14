## Description:

Conclave is a multi-agent reasoning skill that orchestrates multiple AI CLIs into structured debates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mclyang](https://clawhub.ai/user/mclyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and decision makers use Conclave to run structured multi-agent debates for high-stakes choices such as architecture selection, contract risk, pricing, and investment judgment. It produces chair-adjudicated decision reports, minutes, and debate records from multiple AI panelists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and preflight can install or update global CLI packages and tools.

Mitigation: Run the installer with --check-only first, use --skip-update when automatic updates are not acceptable, and review the reported actions before continuing.

Risk: Debate content may be sent to multiple third-party AI services.

Mitigation: Avoid regulated personal data, trade secrets, and classified material unless provider data policies and approvals are already in place.

Risk: Full debate archives persist locally and may be exported into the working directory.

Mitigation: Use cleanup.sh, a retention schedule, or manual deletion of ~/.hermes/debates when debate records should not remain on disk.

Risk: Provider credentials and local authentication must be configured before debates run.

Mitigation: Follow the documented provider setup checks, do not paste passwords into prompts or scripts, and unlock platform keychains interactively when required.

## Reference(s):

- [Conclave Consensus Protocol](artifact/references/consensus-protocol-v1.md)
- [Panelist Roster](artifact/references/panelists.md)
- [ClawHub Skill Page](https://clawhub.ai/mclyang/skills/conclave-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, meeting minutes, debate files, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Debate records are persisted locally and may be copied into the working directory unless the user cleans them up.]

## Skill Version(s):

1.6.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

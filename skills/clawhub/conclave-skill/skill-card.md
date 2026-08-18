## Description:

Conclave is a multi-agent reasoning skill that orchestrates multiple AI CLIs into structured debates, where agents independently analyze a problem, challenge competing arguments, identify flaws and contradictions, and refine reasoning through multiple rounds of discussion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mclyang](https://clawhub.ai/user/mclyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and decision makers use this skill to run structured multi-agent debates for high-stakes decisions such as architecture selection, contract risk, pricing structure, and investment judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad environment changes through global CLI installation and update workflows.

Mitigation: Review installation output before proceeding, use check-only or skip-update modes where possible, and install in an environment where global CLI changes are acceptable.

Risk: Debate prompts and summaries can be sent to multiple third-party AI providers.

Mitigation: Avoid regulated, classified, trade-secret, or personal data unless provider policies have been reviewed and the disclosure is approved.

Risk: Full debate records are retained locally and exported to the working directory.

Mitigation: Run debates from an isolated, non-public directory and use the cleanup script or manual deletion to manage retention.

## Reference(s):

- [README](README.md)
- [Consensus Protocol](references/consensus-protocol-v1.md)
- [Panelist Roster](references/panelists.md)
- [Conclave Skill Page](https://clawhub.ai/mclyang/skills/conclave-skill)
- [Manus Tasks API](https://api.manus.im/v1/tasks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, debate records, shell command invocations, and configuration checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent debate archives and deliverables such as final.md, minutes.md, and index.md.]

## Skill Version(s):

1.6.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

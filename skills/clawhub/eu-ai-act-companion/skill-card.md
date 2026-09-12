## Description:

EU AI Act Companion helps agents classify an AI use case by EU AI Act risk level, summarize role-based obligations, and surface key compliance milestones using local skill guidance and a heuristic CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, product teams, and compliance reviewers use this skill to triage EU AI Act risk level, role-specific obligations, conformity assessment paths, and key deadlines before placing or deploying AI systems in the EU market.

### Deployment Geography for Use:

Global, with subject matter focused on AI systems placed on the EU market or deployed in the EU.

## Known Risks and Mitigations:

Risk: The documented global install command relies on mutable, unpinned third-party retrieval.

Mitigation: Install only from a trusted source and revision; review or pin the repository commit and installer version before global installation.

Risk: The skill provides heuristic compliance navigation and may not reflect every official EU AI Act requirement for a regulated use case.

Mitigation: Use the output as triage guidance only and have critical or regulated decisions reviewed against the latest official requirements by qualified humans.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/eu-ai-act-companion)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [Skill README](README.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and command-line text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, zero-dependency Python CLI with deterministic keyword-based classification; outputs are a compliance aid, not legal advice.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.2.0 and manifest says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

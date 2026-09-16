## Description:

Define and use segments, which are named saved filters over a Cargo model used as the audience for a batch run, play trigger, export, or similar downstream workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and go-to-market teams use this skill to inspect, create, update, and troubleshoot Cargo audience segments before running downstream actions such as batches, plays, exports, or change monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs @cargo-ai/cli@latest, which can change over time.

Mitigation: Use a pinned and reviewed Cargo CLI version for controlled deployments.

Risk: Authenticated commands can create, update, remove, fetch, or download Cargo workspace segment data.

Mitigation: Use the least-privileged Cargo token or account available and confirm the active workspace before running write or download commands.

Risk: Segment download commands can return signed URLs for full datasets.

Mitigation: Treat download URLs as sensitive access links and avoid sharing or logging them unnecessarily.

## Reference(s):

- [Segmentation response shapes](references/response-shapes.md)
- [Segmentation troubleshooting](references/troubleshooting.md)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-segmentation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands emit JSON and may create, update, remove, fetch, or download authenticated Cargo workspace segment data.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

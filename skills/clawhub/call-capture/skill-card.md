## Description:

Automates daily capture of recorded sales calls into raw call archives, structured call logs, and reviewable context updates through a pull request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operations teams use this skill to install and adapt a scheduled call-scribing workflow that turns recorded customer calls into repository-backed cadence logs and context updates. The workflow is intended for teams that want repeated sales-call insights promoted into shared knowledge only after human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw call transcripts and notes can contain sensitive customer, prospect, or internal information.

Mitigation: Install only in a repository approved for raw call transcript storage, set the internal email domain correctly, and review generated pull requests before merge.

Risk: The workflow needs recorder API credentials and a GitHub write path to create branches and pull requests.

Mitigation: Keep the recorder API key in secret-backed configuration, verify the GitHub connector can write only to the intended repository, and do not hard-code credentials.

Risk: Incorrect recorder adapter fields or readiness checks can produce clean but empty runs.

Mitigation: Validate recorder responses against the live API, run the collector with --dry-run before deployment, and monitor pull request capture counts.

Risk: Generated context updates could promote inaccurate or single-call claims into shared knowledge.

Mitigation: Require two independent occurrences, cite source call logs, preserve the pull request review gate, and never let the agent merge its own changes.

Risk: Unpinned local tooling can change collection behavior between runs.

Mitigation: Pin the local tsx and related tooling dependencies used by the collector.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/call-capture)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Call capture cookbook source](https://github.com/getcargohq/gtm-skills/tree/main/call-capture)
- [Recorder provider reference](references/providers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces repository changes as a reviewable pull request; generated call logs and context updates should be reviewed before merge.]

## Skill Version(s):

0.1.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

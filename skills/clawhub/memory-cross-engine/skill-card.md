## Description:

Memory Cross Engine provides a local structured memory bus so planning, memory, verification, and reflection engines can share, link, retrieve, and inspect task context across longer agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect planner, memory, verification, and reflection components through shared local memory during long-horizon tasks. It supports writing structured entries, linking related records, retrieving relevant context, filtering by engine, and viewing cross-engine memory coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists task memory, errors, and preferences across runs, which may retain private prompts, business data, or personal preferences.

Mitigation: Review before installation, avoid storing sensitive data unless retention is acceptable, and inspect or delete generated memory and learned-pattern files when data should not persist.

Risk: The artifact does not clearly define consent, retention, deletion, redaction, or scoping controls for retained memory.

Mitigation: Establish explicit opt-in, retention, deletion, and redaction procedures before using the skill in shared, customer-facing, or sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/memory-cross-engine)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON/text memory records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference local JSONL memory records and learned preference data created by the bundled scripts.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

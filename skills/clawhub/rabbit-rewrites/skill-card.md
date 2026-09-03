## Description:

Rewrite flagged prose using a small local model over an OpenAI-compatible endpoint, with planning, gated in-place rewrites, and model benchmarking support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whit3rabbit](https://clawhub.ai/user/whit3rabbit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writers use this skill to scan prose, plan targeted rewrite requests, apply model-backed edits through configured local or OpenAI-compatible endpoints, and benchmark small models for rewriting quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional model-endpoint use can send flagged passages to a configured endpoint.

Mitigation: Use local or HTTPS endpoints, preview with --model-plan or --stdout and diff before --write, and keep API keys in dedicated RABBIT_* environment variables.

Risk: The bundled Claude hook can automatically change commit and PR messages when wired into Claude Code hooks.

Mitigation: Review scripts/claude_hook.py before enabling hook integration and install only when that behavior is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whit3rabbit/skills/rabbit-rewrites)
- [Models and Download Locations](references/models.md)
- [Security notes for reviewers and scanners](SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and rewritten prose output from configured commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit rewrite plans, stdout diffs, benchmark JSON, or in-place file edits depending on the selected command flags.]

## Skill Version(s):

0.5.0 (source: frontmatter metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

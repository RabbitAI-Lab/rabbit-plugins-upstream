## Description:

Analyzes a user's own Xiaohongshu creator-backend analytics, benchmarks recent notes against public high-performing notes in similar topics, and generates an account diagnosis report with funnel metrics and concrete improvement actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and operator-agents use this skill to diagnose recent Xiaohongshu note performance using the account owner's official creator-backend export. It helps identify funnel drop-offs, compare each note with public same-topic high-performing notes, and produce action-oriented recommendations for future content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles private creator-account analytics through a logged-in Chrome session and writes business metrics to local files.

Mitigation: Run it only in a trusted local environment, review generated files before sharing, and clean up sensitive reports when they are no longer needed.

Risk: The security evidence flags an obfuscated helper that can send prompts to a configurable LLM endpoint with unclear data-flow limits.

Mitigation: Use only trusted publisher and dependency versions, review or replace the helper with readable code, and allowlist the intended LLM endpoint before execution.

Risk: The workflow depends on webclaw3 browser relay and pipeline services that reuse the user's active browser session.

Mitigation: Install webclaw3 from trusted sources, verify the local runtime configuration, and avoid running the skill while logged into accounts unrelated to the analysis task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-note-analyst)
- [webclaw3 browser automation dependency](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [webclaw3 installation guide](https://github.com/fatmind/webclaw3)

## Skill Output:

**Output Type(s):** [Analysis, Files, Markdown, JSON, Guidance]

**Output Format:** [HTML report, JSON status summary, Markdown data report, and stdout JSON summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local report_path, res.json, and data.md outputs; reports may contain private creator-account metrics and benchmark-derived recommendations.]

## Skill Version(s):

1.1.4 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

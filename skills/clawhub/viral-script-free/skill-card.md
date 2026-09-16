## Description:

Analyzes a spoken video transcript offline and returns a structural map, hook assessment, retention pacing diagnosis, speakability score, CTA strength, and a severity-ranked issue list, with the free release limited to the overview, structure map, and first three issue titles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators and marketers use this skill to check spoken short-video scripts for structure, opening hook strength, pacing, oral style, and CTA placement before revising or publishing. It is intended for mechanical script diagnostics, not claims about virality, legal compliance, platform approval, or commercial performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact documentation includes a paid full-version purchase path and an unpinned installer command outside the free checker's core purpose.

Mitigation: Use the free local checker only after review, and require separate explicit approval before any agent runs the installer, follows newly installed SkillPay instructions, or starts a purchase workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/viral-script-free)
- [Hook pattern reference](references/hook-patterns.md)
- [Platform pacing reference](references/platform-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown-style terminal text or JSON, depending on invocation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free release exposes the summary, structure map, and first three issue titles while withholding detailed locations, rule basis, rewrite suggestions, golden-line candidates, and remix blueprint.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

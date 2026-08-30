## Description:

Delegates tasks to Gemini CLI implementing delegation-core for Google's models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when delegation-core selects Gemini CLI for large-context file analysis, batch processing, summarization, or pattern extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gemini CLI file references and broad glob patterns can send local file contents to Google/Gemini.

Mitigation: Review selected files before delegation and avoid broad globs over secrets, private repositories, or sensitive business data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-gemini-delegation)
- [Configured project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide Gemini CLI calls that include local file references or glob patterns.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

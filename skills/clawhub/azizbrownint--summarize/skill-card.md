## Description:

Summarize or transcribe URLs, YouTube/videos, podcasts, articles, transcripts, PDFs, and local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent call the summarize CLI for concise summaries or best-effort transcripts of web pages, videos, podcasts, PDFs, transcripts, and local files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a Homebrew-installed third-party summarize CLI.

Mitigation: Install only from the expected formula and review the installed CLI before using it in trusted workflows.

Risk: Submitted URLs, local files, or transcripts may be processed by configured model providers or optional extraction services.

Mitigation: Avoid sensitive files and private URLs unless provider settings, optional services, and intended API keys have been reviewed.

Risk: Optional API keys for model and extraction providers can expand the data shared outside the local environment.

Mitigation: Expose only the provider credentials required for the current task and disable optional extraction services when they are not needed.

## Reference(s):

- [summarize homepage](https://summarize.sh)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/summarize)
- [ClawHub publisher profile](https://clawhub.ai/user/azizbrownint)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the underlying CLI can also emit JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output length, token budget, extraction mode, YouTube handling, and optional extraction services can be configured with CLI flags.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

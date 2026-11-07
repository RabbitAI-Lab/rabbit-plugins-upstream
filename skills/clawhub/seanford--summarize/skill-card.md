## Description:

Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube).

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent guide use of the summarize CLI for summarizing URLs, local files, images, audio, and YouTube links with a selected model provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on installing and running a third-party summarize CLI.

Mitigation: Install only from a trusted distribution channel and review the CLI package before use in managed environments.

Risk: Selected URLs, files, images, audio, or YouTube content may be sent to configured model or extraction providers.

Mitigation: Do not use the skill on sensitive, regulated, or private content unless those provider transfers are approved.

Risk: Provider API keys are required for some model and extraction services.

Mitigation: Store API keys in approved secret-management or environment-variable workflows and avoid committing them to shared configuration files.

## Reference(s):

- [Summarize homepage](https://summarize.sh)
- [ClawHub skill page](https://clawhub.ai/seanford/skills/summarize)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI supports length, maximum token, extraction-only, JSON, Firecrawl, and YouTube fallback options.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Inspect a real public website and design a runnable Dataify-based scraper when no suitable prebuilt scraper exists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect a public target URL, route to an existing Dataify scraper when appropriate, or generate and validate a single-page Web Unlocker scraper starter for requested fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs, search terms, and fetched page content may be sent to Dataify using DATAIFY_API_TOKEN.

Mitigation: Use only public, non-confidential, non-login-protected targets and review organizational data-sharing requirements before running the skill.

Risk: Generated curl previews and scraper starter code may be unsuitable or unsafe to execute without review.

Mitigation: Inspect generated commands and code before execution, especially target URL, output path, request scope, and token handling.

Risk: Fetched sample HTML may be retained in the output directory.

Mitigation: Delete generated sample.html and related output files when fetched content may contain sensitive or restricted data.

Risk: Some helper requests place the Dataify token in URL query parameters.

Mitigation: Run in a trusted environment, avoid exposing logs or command histories, and rotate the token if it may have been disclosed.

## Reference(s):

- [Prebuilt routing](references/prebuilt-routing.md)
- [Dataify documentation](https://doc.dataify.com)
- [Dataify support](https://www.dataify.com/)
- [ClawHub skill listing](https://clawhub.ai/dataify-server/skills/dataify-scraper-builder)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands, JSON status records, and generated Python scraper files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write scraper_spec.json, site_profile.json, sample_output.json, validation.json, sample.html, and generated_scraper.py under the selected output directory.]

## Skill Version(s):

1.1.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

chrome-use gives agents live web access, URL reading, scraping, authenticated browsing, browser automation, screenshots, web-app testing, and workflow-specific guidance through a Chrome/Chromium automation CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leeguooooo](https://clawhub.ai/user/leeguooooo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to browse the web, inspect URLs, automate Chrome/Chromium sessions, capture screenshots, scrape data, test web applications, and reuse authenticated browser state when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reuse logged-in Chrome sessions and persistent browser state.

Mitigation: Use it only with trusted sites and accounts, and confirm that authenticated browsing is intended before exposing sensitive sessions.

Risk: The skill includes automatic remote installation behavior when the local CLI is missing.

Mitigation: Review the installer source and publisher trust before installation, and prefer controlled installation in managed environments.

Risk: The skill positions itself as the default for broad web lookup, scraping, and browser automation tasks.

Mitigation: Route only appropriate web automation tasks to this skill and keep higher-risk actions, form submissions, uploads, and account operations under explicit user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leeguooooo/skills/chrome-use)
- [Publisher profile](https://clawhub.ai/user/leeguooooo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and browser-automation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include screenshots, extracted page data, test observations, and commands for loading version-matched CLI skill content.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

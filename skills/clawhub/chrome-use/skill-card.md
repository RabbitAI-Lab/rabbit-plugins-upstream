## Description:

chrome-use gives agents browser automation through the user's real, logged-in Chrome for live web access, page reading, scraping, authenticated browsing, form interaction, screenshots, extraction, and web app testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leeguooooo](https://clawhub.ai/user/leeguooooo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent needs live browser access, authenticated page interaction, web data extraction, screenshots, or exploratory web application testing in Chrome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to operate inside a real, logged-in Chrome session and may interact with accounts the user is already signed into.

Mitigation: Use it only for tasks where real browser automation is needed, and require explicit confirmation before form submissions, uploads, purchases, settings changes, messages, or other account-affecting actions.

Risk: The artifact includes a remote curl-to-shell installer path.

Mitigation: Avoid automatic installation from the provided command unless the installer has been independently reviewed and verified.

Risk: The security evidence notes dynamic unaudited runtime instructions served by the CLI.

Mitigation: Review the loaded runtime guidance and proposed browser or shell actions before executing sensitive steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leeguooooo/skills/chrome-use)
- [Publisher profile](https://clawhub.ai/user/leeguooooo)
- [Installer script referenced by artifact](https://raw.githubusercontent.com/leeguooooo/chrome-use/main/install.sh)
- [Observability dashboard origin](https://dashboard.chrome-use.localhost)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and browser task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May operate in logged-in browser sessions; require explicit confirmation before account-affecting actions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Automate logged-in browser tasks such as navigating websites, filling forms, capturing screenshots, extracting page data, and testing web apps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[citrolabs](https://clawhub.ai/user/citrolabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users can automate tasks in logged-in websites, inspect page content, and test or troubleshoot web apps through a Chromium browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer changes macOS security protections before launching the downloaded app.

Mitigation: Review the installer before running it; require explicit approval for privileged changes and verify the publisher while retaining normal macOS security checks.

Risk: Cookie-clearing commands can sign the user out of unrelated sites on a shared browser profile.

Mitigation: Use exact cookie name, domain, and path selection or clear data for a single origin; obtain approval before any profile-wide clear.

Risk: The downloaded browser and runtime-generated instructions were not assessed in the supplied security review.

Mitigation: Review and verify those components separately before relying on them.

## Reference(s):

- [Install or upgrade ego lite](references/install.md)
- [Clearing cookies, cache, and storage](references/clearing-state.md)
- [ego lite website](https://lite.ego.app/)
- [ClawHub skill page](https://clawhub.ai/citrolabs/skills/ego-browser)

## Skill Output:

**Output Type(s):** [Guidance, Browser actions, Extracted data, Shell commands, Code]

**Output Format:** [Markdown guidance, shell commands, JavaScript snippets, and structured browser results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the ego lite browser and may use the user's logged-in browser profile.]

## Skill Version(s):

2.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

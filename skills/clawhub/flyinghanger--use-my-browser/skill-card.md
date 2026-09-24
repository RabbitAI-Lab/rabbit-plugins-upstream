## Description:

Controls the user's real Chrome browser through Tampermonkey injection so an agent can navigate pages, read visible content, interact with elements, and run page-context JavaScript using existing login sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyinghanger](https://clawhub.ai/user/flyinghanger)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when an agent needs to operate a real logged-in Chrome session, including reading pages, navigating tabs, filling forms, clicking controls, and extracting page data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad control over pages open in a logged-in Chrome session.

Mitigation: Use a separate browser profile with limited logins, restrict use to intended tabs and sites, and avoid banking, identity, healthcare, admin, or other high-risk sites unless every action is explicitly directed.

Risk: The setup relies on browser-control components that are not pinned in the artifact instructions.

Mitigation: Review or pin the Tampermonkey userscript and plugin versions before setup, and reinstall only from trusted sources.

Risk: Page-context JavaScript can read page data or trigger authenticated actions.

Mitigation: Review proposed JavaScript and browser actions before execution, especially form submissions, account changes, downloads, or data extraction from sensitive pages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyinghanger/skills/use-my-browser)
- [Tampermonkey userscript](https://raw.githubusercontent.com/lsdefine/pc-agent-loop/main/assets/ljq_web_driver.user.js)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return page text, simplified HTML, interactive element lists, or JavaScript return values through the browser-control tools.]

## Skill Version(s):

1.0.0 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

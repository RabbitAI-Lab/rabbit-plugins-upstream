## Description:

Automates an already logged-in Edge or Chrome browser over the Chrome DevTools Protocol for navigation, JavaScript-rendered page interaction, DOM extraction, screenshots, and related browser tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hunling233](https://clawhub.ai/user/hunling233)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when static fetching is insufficient, especially for JavaScript-rendered pages, authenticated browser sessions, interactive workflows, screenshots, and structured extraction from a live browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly control a logged-in browser session, including pages and accounts available in that profile.

Mitigation: Use an isolated automation browser profile rather than a daily profile, and confirm before form submissions, downloads, purchases, account changes, or other sensitive actions.

Risk: Browser cookies, tabs, downloads, and forced browser restarts are under-scoped in the skill guidance.

Mitigation: Avoid reading browser cookie databases, close or clean the automation profile after use, and review active tabs and downloaded files before trusting outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hunling233/skills/browser-automation-cdp)
- [SKILL.md](artifact/SKILL.md)
- [REFERENCE.md](artifact/REFERENCE.md)
- [EXAMPLES.md](artifact/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance, JSON, Screenshots]

**Output Format:** [Markdown guidance with JavaScript and shell command examples, JSON command results, and base64 or file-based PNG screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May act through a live browser profile, reuse authenticated sessions, and create downloaded files or screenshots depending on the requested automation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

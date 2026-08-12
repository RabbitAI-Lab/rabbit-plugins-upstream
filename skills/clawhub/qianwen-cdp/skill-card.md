## Description:

Drives the Qianwen desktop browser through native Chrome DevTools Protocol, reusing a real logged-in profile for browser automation tasks such as opening pages, filling forms, clicking, extracting content, and capturing screenshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to automate Qianwen browser sessions that need the user's existing login state. It is intended for local browser actions such as navigation, form entry, page inspection, content extraction, and screenshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act inside an authenticated Qianwen browser profile, including reading private page content and performing clicks or text entry as the logged-in user.

Mitigation: Install only for trusted local automation workflows, review intended actions before use, and require explicit user approval before external posting, messaging, or data-changing actions.

Risk: Persistent CDP debugging access can expose browser state and authenticated sessions to local processes that can reach the debugging port.

Mitigation: Enable the debugging port only when needed, understand which profile is used, and remove shortcut changes or close the browser when automation is complete.

Risk: The shortcut patcher can alter Windows .lnk files to keep the Qianwen debugging port enabled.

Mitigation: Run shortcut patching deliberately, keep a record of modified shortcuts, and use the provided unapply behavior or manual shortcut review to remove the debugging argument.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/qianwen-cdp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-like command results; screenshots are written as image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate against a local Qianwen browser profile and may produce page text, links, input metadata, target identifiers, or screenshot paths.]

## Skill Version(s):

0.1.1 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

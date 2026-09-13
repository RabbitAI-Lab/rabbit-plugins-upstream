## Description:

Drive the browser the user is already signed into, instead of a cold automation profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agents use this skill to automate browser tasks that require an existing signed-in session, such as internal dashboards, account pages, rendered CSS inspection, React state inspection, full-page capture, or replaying live UI flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate in a real signed-in browser session where actions may affect user accounts or data.

Mitigation: Read the current page state before acting, confirm irreversible actions with the user, and verify results after each action.

Risk: The setup asks users to install a browser bridge and extension that can automate live sessions.

Mitigation: Install only from trusted sources, pin the npm package to a reviewed exact version where possible, avoid unnecessary global installation, and restrict extension access to the minimum required sites.

Risk: Permissive automation defaults can allow high-risk actions without repeated prompts.

Mitigation: Leave high-risk approval prompts enabled and do not use signed-in browser automation for public pages that ordinary fetching or isolated browser automation can handle.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/t3rnel-signed-in-browser)
- [T3rnel Browser documentation](https://t3ratech.github.io/t3rnel-browser-plugin/)
- [T3rnel Browser tools documentation](https://t3ratech.github.io/t3rnel-browser-plugin/tools.html)
- [Chrome Web Store extension](https://chromewebstore.google.com/detail/egpckhdpkoeimoekciejbmbbcackhdmd)
- [Microsoft Edge add-on](https://microsoftedge.microsoft.com/addons/detail/t3rnel-browser/dnplmolfblplbeclnglmjamppekpbcjo)
- [Firefox add-on](https://addons.mozilla.org/en-US/firefox/addon/t3rnel-browser/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operating guidance for MCP browser tools and safety checks before actions in live signed-in sessions.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

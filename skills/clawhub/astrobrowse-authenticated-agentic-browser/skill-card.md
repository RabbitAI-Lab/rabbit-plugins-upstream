## Description:

AstroBrowse lets an agent operate a real authenticated browser session for user-approved websites and accounts, including logged-in SaaS workflows, form fills, reports, downloads, screenshots, and human takeover when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let agents complete multi-step workflows in logged-in web apps that lack APIs, such as posting content, updating CRM or ERP records, filling forms, downloading files, and extracting page data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can take real actions in logged-in accounts.

Mitigation: Use narrowly scoped tasks, confirm before public posts, record changes, submissions, downloads, screenshots, or recordings, and rely on human takeover for MFA, CAPTCHA, unusual login flows, or judgment-sensitive steps.

Risk: Session artifacts such as downloads, screenshots, and recordings may persist outside the browser session.

Mitigation: Avoid sensitive accounts unless File Manager retention and access controls fit the use case, and close the browser when the workflow is complete.

Risk: Automation may act on the wrong page state or selector in a live account.

Mitigation: Use stable selectors, split longer workflows into bounded step batches, and verify state with extraction or screenshots before consequential actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/astrobrowse-authenticated-agentic-browser)
- [AgentPMT marketplace page](https://www.agentpmt.com/marketplace/astrobrowse-authenticated-agentic-browser)
- [AstroBrowse setup guide](https://www.agentpmt.com/docs/tool-specific/astrobrowse)
- [Schema reference](artifact/schema.md)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, code, API calls]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers action names, parameter schemas, browser session handling, file artifacts, screenshots, downloads, recordings, and human takeover.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

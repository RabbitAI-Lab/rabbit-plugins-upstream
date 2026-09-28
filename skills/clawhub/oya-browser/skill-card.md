## Description:

Guides agents in using Oya Browser to navigate and automate websites in persistent cloud Chrome sessions through MCP tools, a CLI, or an SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oyaaiprod](https://clawhub.ai/user/oyaaiprod)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can direct an agent to browse sites, complete forms, extract page information, and automate web workflows using Oya Browser. Persistent personas can retain logged-in sessions across runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser personas may access logged-in accounts, stored credentials, and private data during broad browsing tasks.

Mitigation: Set clear task and site limits; require confirmation before credential use, MFA completion, or scraping authenticated content.

Risk: Automated browser actions may submit forms, make purchases, or change account settings without sufficient review.

Mitigation: Require user confirmation before submissions, destructive changes, purchases, or moderation actions.

Risk: Running browser sessions may incur costs and preserve account state.

Mitigation: Stop browsers after use and review access to persistent personas.

## Reference(s):

- [Oya Browser documentation](https://oyabrowser.com/docs)
- [Oya Browser agent guidance](https://oyabrowser.com/llms.txt)
- [Oya Browser ClawHub release](https://clawhub.ai/oyaaiprod/skills/oya-browser)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with command and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include page summaries, extracted content, and browser automation steps.]

## Skill Version(s):

1.0.125 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

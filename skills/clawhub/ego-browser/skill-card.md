## Description:

ego-lite Windows browser automation skill that lets an AI agent control browser workflows with natural language, including login-aware navigation, scraping, form filling, and isolated multi-Space tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawhub-master](https://clawhub.ai/user/clawhub-master)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to automate Windows browser workflows across logged-in SaaS, CRM, internal systems, repetitive form tasks, and multi-site scraping. It is intended for agent-driven browser actions where semantic snapshots, isolated browser Spaces, and explicit confirmation for sensitive actions are useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control browser pages in logged-in SaaS or internal sites.

Mitigation: Use test or least-privilege accounts where possible and review browser actions before granting access to sensitive sessions.

Risk: Browser automation may trigger destructive, public, payment, or other high-impact actions.

Mitigation: Require human confirmation before payments, deletion, publishing, or comparable high-risk operations.

Risk: Persisted site learnings could accidentally store passwords, tokens, personal data, or sensitive business content.

Mitigation: Keep learnings limited to operational notes and exclude credentials, tokens, personal data, and confidential business content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clawhub-master/skills/ego-browser)
- [learnings README](learnings/README.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JavaScript, PowerShell, and shell command examples; runtime output may be plain text or JSON logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include executable browser automation scripts and page-derived observations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

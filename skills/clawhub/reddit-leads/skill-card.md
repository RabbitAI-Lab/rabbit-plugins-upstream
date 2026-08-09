## Description:

Discover B2B leads from Reddit using AI-powered lead scoring via reddapi.dev Leads API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and founder teams use this skill to find high-intent B2B prospects in public Reddit discussions, prioritize them by lead score and lead type, and prepare research or outreach drafts for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public Reddit discussions used for prospecting can raise platform-policy and privacy-expectation concerns.

Mitigation: Review Reddit and platform policies before use, and keep outreach decisions under human review.

Risk: Lead titles, bodies, comments, URLs, and file paths are unmoderated third-party content and may contain misleading or prompt-like text.

Mitigation: Treat lead content as evidence only, quote it separately from agent output, and do not fetch URLs or execute commands from results.

Risk: The reddapi.dev API key could be exposed if pasted into chat, logged, echoed, or written to files.

Mitigation: Keep REDDAPI_API_KEY in the user's shell environment, use REDDAPI_AUTH for requests, and never print, store, or repeat the key.

Risk: Lead scores and classifications can be over-relied on for outreach, CRM writes, or other external actions.

Mitigation: Use scores as research input only; draft outreach for the user to review and send manually.

## Reference(s):

- [reddapi.dev Leads API](https://reddapi.dev/leads)
- [reddapi.dev API base](https://reddapi.dev)
- [reddapi.dev account and API keys](https://reddapi.dev/account)
- [ClawHub Reddit Leads listing](https://clawhub.ai/lignertys/skills/reddit-leads)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses REDDAPI_AUTH from the shell environment and treats lead result content as untrusted third-party text.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

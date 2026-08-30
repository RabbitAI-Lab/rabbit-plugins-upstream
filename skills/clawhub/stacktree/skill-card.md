## Description:

Publish HTML produced by an agent to private Stacktree links for browser sharing, with free temporary publishing, optional passcodes, paid permanent pages, and wallet-based updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevysmith](https://clawhub.ai/user/stevysmith)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and personal-agent operators use this skill to publish reports, dashboards, briefs, visualizations, and standing pages as shareable Stacktree links. It is especially suited for agent-generated HTML that needs to be opened in a browser instead of delivered as a chat attachment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet private keys and stk_live_ API keys are sensitive credentials used by the Stacktree publishing and update flows.

Mitigation: Keep credentials out of chat transcripts, command arguments, and logs; prefer the default wallet file flow and store API keys securely.

Risk: Using an unintended Stacktree endpoint can expose content or credentials to an untrusted service.

Mitigation: Use the default stacktr.ee endpoint unless there is an intentional trust decision to use another endpoint.

Risk: Updating the wrong site ID can change content behind a public or client-facing link.

Mitigation: Confirm the site ID before updating an existing page, especially for standing dashboards or deliverables.

Risk: Viewer feedback or reactions can contain prompt-injection attempts.

Mitigation: Treat viewer-provided text strictly as data to report back to the human, not as instructions for the agent to follow.

## Reference(s):

- [Stacktree homepage](https://stacktr.ee)
- [Stacktree x402 agent documentation](https://stacktr.ee/x402.md)
- [Stacktree authentication documentation](https://stacktr.ee/auth.md)
- [Stacktree agent map](https://stacktr.ee/agent.txt)
- [ClawHub skill page](https://clawhub.ai/stevysmith/skills/stacktree)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API request examples, and JSON response handling guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce curl, npx, node, and npm commands for publishing or updating Stacktree pages.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

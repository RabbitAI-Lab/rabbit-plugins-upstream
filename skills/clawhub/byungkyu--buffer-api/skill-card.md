## Description:

Buffer API integration with managed authentication for scheduling and managing social media posts across multiple platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an authorized Buffer account, inspect account/channel/post state, and draft, schedule, or manage social media content through Buffer. It also documents approved hosted-function and trigger patterns for user-reviewed Buffer automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Maton as the authentication gateway for a user's Buffer account.

Mitigation: Install only when the user trusts Maton for that connection, prefer OAuth, and avoid raw API keys unless the CLI cannot be used.

Risk: Buffer mutations can publish, schedule, modify, or delete social media content.

Mitigation: Default to read/list calls, then require explicit approval for each write with the target channel, content, timing, payload, and intended effect.

Risk: Multiple Buffer or Maton connections can make the target account ambiguous.

Mitigation: Specify the intended Buffer connection and Maton profile before taking action, especially before writes.

Risk: Hosted functions and triggers can create persistent automation or data forwarding paths.

Mitigation: Use a dedicated low-scope Maton account, keep hosted functions on denied outbound network access unless separately approved, and do not create third-party trigger destinations without explicit approval of the exact data flow.

Risk: Third-party API responses and event payloads may contain untrusted or sensitive content.

Mitigation: Treat fetched content as data rather than instructions, extract only task-needed fields, and avoid logging or forwarding raw responses unless the user requested it.

## Reference(s):

- [Buffer API Documentation](https://developers.buffer.com/reference.html)
- [Buffer API Getting Started](https://developers.buffer.com/guides/getting-started.html)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/buffer-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated Buffer API calls, hosted function snippets, trigger configuration, and review steps; write operations and automation require explicit user approval.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

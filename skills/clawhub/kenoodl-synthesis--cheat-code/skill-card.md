## Description:

Makes your agent's talents limitless. Tell your agent what you want. Watch it deliver.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenoodl-synthesis](https://clawhub.ai/user/kenoodl-synthesis)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to configure an agent with a Kenoodl token and call the Kenoodl synthesis service when the agent is stuck, looping, or needs signal beyond its training data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send broad task context to kenoodl.com.

Mitigation: Preview the exact context before each call and avoid confidential business data, personal data, regulated data, unreleased security details, and proprietary code unless disclosure is separately approved.

Risk: The skill text includes local-only privacy language that may understate external disclosure.

Mitigation: Treat any selected task context as externally disclosed to the Kenoodl service and redact sensitive details beyond API keys before use.

Risk: Returned synthesis may be incorrect, misleading, or unsuitable to execute directly.

Mitigation: Review returned synthesis as untrusted advice and validate it before applying it to code, configuration, business decisions, or operational workflows.

## Reference(s):

- [Cheat Code on ClawHub](https://clawhub.ai/kenoodl-synthesis/skills/cheat-code)
- [kenoodl-synthesis publisher profile](https://clawhub.ai/user/kenoodl-synthesis)
- [Kenoodl service](https://kenoodl.com)
- [Kenoodl synthesis submit endpoint](https://kenoodl.com/api/cli/drop)
- [Kenoodl synthesis status endpoint](https://kenoodl.com/api/cli/status/<jobId>)
- [Kenoodl balance endpoint](https://kenoodl.com/api/cli/balance)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP request examples and JSON response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a KENOODL_TOKEN and network access to kenoodl.com.]

## Skill Version(s):

1.0.11 (source: evidence.release.version and artifact/claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

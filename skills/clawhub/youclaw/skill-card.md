## Description:

YouClaw is a YouCloud marketing analysis assistant that breaks down ad creatives, uncovers brand advertising strategies, and supports strategy exploration, creative critique, stress testing, and creative polishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcloud](https://clawhub.ai/user/youcloud)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, agencies, and growth strategists use this skill to send brand, competitor, and ad creative prompts to YouCloud's YouShu AI API and receive marketing strategy analysis or iterative creative critique.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User prompts for marketing analysis are sent to YouCloud's API.

Mitigation: Confirm the intended data sharing before use and avoid sending confidential or sensitive marketing information unless that is acceptable under the user's policies.

Risk: The skill requires a user-supplied YOUCLOUD_API_KEY in the environment.

Mitigation: Store the API key only in appropriate secret or environment management systems and rotate it if it may have been exposed.

Risk: Automatic trigger phrases and multiple slash commands can select different analysis modes.

Mitigation: Use explicit commands such as /youclaw, /creative-chat, or /grill when predictable behavior is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youcloud/skills/youclaw)
- [YouCloud homepage](https://www.youcloud.com)
- [YouShu AI API endpoint](https://aichat.youshu.youcloud.com/aichat/claw)
- [Usage example](references/example.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown analysis reports, follow-up guidance, configuration instructions, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires YOUCLOUD_API_KEY and may preserve a session_id for follow-up questions.]

## Skill Version(s):

1.2.3 (source: server release evidence; artifact frontmatter says 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

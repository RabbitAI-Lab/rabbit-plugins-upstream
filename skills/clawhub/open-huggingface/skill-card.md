## Description:

Open Hugging Face in the user's Brave browser and take the user to the Hugging Face homepage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to open Hugging Face in Brave, reuse an existing matching tab or session when available, and confirm the expected site is loaded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may reuse an existing authenticated Brave session for Hugging Face.

Mitigation: Install only when this browser automation behavior is desired, and rely on the skill's stop-at-login behavior if authentication is required.

Risk: Browser automation could navigate to or report on the wrong destination if not checked.

Mitigation: The skill requires destination verification before reporting success.

Risk: Credential handling would increase account risk.

Mitigation: The skill states that it does not enter passwords, authentication codes, API keys, or other credentials.

## Reference(s):

- [Hugging Face](https://huggingface.co/)
- [ClawHub Skill Page](https://clawhub.ai/ruchir17-cmd/skills/open-huggingface)
- [Publisher Profile](https://clawhub.ai/user/ruchir17-cmd)

## Skill Output:

**Output Type(s):** [guidance, text, configuration]

**Output Format:** [Markdown or plain text instructions with browser navigation status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reuse an existing authenticated Brave session; does not handle credentials.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

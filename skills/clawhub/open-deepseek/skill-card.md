## Description:

Opens Brave browser and navigates to DeepSeek website when the user says "open deepseek" or "go to deepseek".

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill as an assistant-triggered shortcut to open DeepSeek Chat in Brave when they explicitly request it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User prompts or data entered into the opened DeepSeek page are handled by DeepSeek.

Mitigation: Use the shortcut only when DeepSeek is an approved destination for the information being entered.

Risk: The Windows launcher uses shell=True, which is a harder-to-audit command launch pattern.

Mitigation: Review the submitted script before installation and prefer a hardened launcher implementation for managed environments.

## Reference(s):

- [DeepSeek Chat](https://chat.deepseek.com)
- [Brave Browser](https://brave.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Text status messages and command execution through Python or Bash scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Brave browser and either Python 3 or Bash on a supported desktop operating system.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/config.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

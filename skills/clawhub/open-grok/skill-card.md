## Description:

Opens Brave browser to Grok AI by xAI (Elon Musk's company). Access the witty, real-time AI with a simple voice command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to open Grok in Brave from agent trigger phrases when they want to chat with Grok or compare responses across AI assistants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may open Grok unintentionally.

Mitigation: Review and narrow trigger phrases before deployment if accidental browser launches would disrupt the user.

Risk: The Windows launch path uses shell=True.

Mitigation: Replace the Windows browser-opening command with a safer launch method before adapting the script for broader or higher-trust environments.

Risk: The skill depends on local Brave installation, network access, and Grok account eligibility.

Mitigation: Confirm these prerequisites before enabling the skill and provide fallback guidance when Brave or Grok access is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ruchir17-cmd/skills/open-grok)
- [Grok](https://grok.x.ai)
- [Brave Browser](https://brave.com)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Browser launch action with a short text status message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Brave browser, network access, an X/Twitter account, and Grok access.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

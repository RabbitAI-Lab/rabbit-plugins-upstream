## Description:

Onboards merchants into the Auto Google Review Reply product by guiding account access, Google Business Profile connection, free-trial or membership checks, and AI review auto-reply configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cheaplightstore](https://clawhub.ai/user/cheaplightstore)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants and support agents use this skill to complete onboarding for an automated Google review reply service, including sign-in, Google Business authorization, location binding, membership validation, and reply-rule setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authenticate to a merchant backend and handle long-lived merchant authorization values.

Mitigation: Review before installation, keep tokens out of chat, URLs, and logs, store only the full Authorization header in the designated environment variable, and mask token values during diagnostics.

Risk: The skill can connect or disconnect Google Business Profile access, bind locations, and configure public-facing automatic review replies.

Mitigation: Confirm the merchant's intended Google Business account, selected location, membership status, reply threshold, language, keywords, and enabled status before making changes.

Risk: Unsafe URL-based token flows may expose credentials if used directly.

Mitigation: Prefer the SSO handoff flow where OAuth tokens are exchanged server-side and can be revoked promptly; avoid asking users to paste passwords, raw tokens, or token-bearing URLs into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cheaplightstore/skills/google-autoreply-setup)
- [Auto Google Review Reply backend API base](https://apprest.mytruststores.com/adminServer)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions, Shell commands]

**Output Format:** [Markdown with API request details and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce step-by-step onboarding instructions, backend API call guidance, OAuth handoff instructions, membership checks, and auto-reply configuration payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

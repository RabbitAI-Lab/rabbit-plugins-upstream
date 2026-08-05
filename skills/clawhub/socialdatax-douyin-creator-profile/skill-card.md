## Description:

Helps agents look up public Douyin creator profile data, including account basics, creator positioning, homepage information, and audience scale, through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public Douyin creator profile facts by sec_user_id, profile URL, short link, or share text. It is suited for profile lookup, audience-scale checks, and separating returned profile facts from later strategic interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a SocialDataX API key and may consume paid balance or credits during repeated profile lookups.

Mitigation: Install only when SocialDataX usage is intended, keep SOCIALDATAX_API_KEY scoped to the correct account, and review billing or balance behavior before repeated use.

Risk: Returned creator profile data is third-party API data and may be incomplete, stale, or unsuitable for unsupported inferences.

Mitigation: Report profile fields as returned facts, preserve API errors, and separate factual profile data from any strategic interpretation.

Risk: Insufficient-balance responses can trigger repeated failed calls if retried blindly.

Mitigation: Do not retry insufficient-balance errors repeatedly; show the recharge URL exactly as returned and continue only after the user confirms recharge.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-profile)
- [devinchen2014 publisher profile](https://clawhub.ai/user/devinchen2014)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and node/npm; profile lookups use either sec_user_id or profile-url input.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

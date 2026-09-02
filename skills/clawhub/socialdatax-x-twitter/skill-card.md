## Description:

Provides an X/Twitter data assistant for content search, post details, comment analysis, creator profiles, and creator post lists using SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research public X/Twitter posts, comments, replies, and creator profiles through SocialDataX when they have a SOCIALDATAX_API_KEY.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and identifiers are sent to SocialDataX using the user's API key.

Mitigation: Use the skill only for approved X/Twitter research data and avoid submitting sensitive or proprietary query content unless that use is authorized.

Risk: Running the SocialDataX npm package and API calls may consume paid credits.

Mitigation: Confirm the SOCIALDATAX_API_KEY account and expected credit usage before broad searches, and do not repeatedly retry insufficient-balance responses.

Risk: The skill depends on the third-party socialdatax-skills npm package and SocialDataX API service.

Mitigation: Install and run it only in environments where the user trusts the package, service, and runtime network access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/socialdatax-x-twitter)
- [SocialDataX API Access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI calls can return JSON-formatted SocialDataX data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm; SocialDataX calls may consume paid credits.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents research Instagram content, post details, comments, replies, creator profiles, and creator post lists using SocialDataX data services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve Instagram search results, post details, audience comments, comment replies, creator profile data, and creator post lists for social media research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Instagram research queries to SocialDataX-hosted data services using SOCIALDATAX_API_KEY.

Mitigation: Use it only when sharing those queries with SocialDataX is acceptable, and provide the API key through the environment rather than embedding it in files.

Risk: The direct CLI examples install and run the socialdatax-skills npm package.

Mitigation: Pin a reviewed npm package version in controlled environments instead of relying on @latest.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-instagram)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY and requires Node.js/npm when running the direct CLI.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

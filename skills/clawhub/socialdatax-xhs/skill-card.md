## Description:

Helps agents research Xiaohongshu trends, notes, comments, and creators through SocialDataX read-only data tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to explore Xiaohongshu search trends, find and examine notes and comments, and review creator profiles and posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime use of an unpinned npm package with an API key may expose users to unexpected package changes.

Mitigation: Review the skill and package source before installing; pin a trusted package version where possible and protect the API key.

Risk: Private XHS links or returned full URLs may contain query tokens that are shared when forwarded.

Mitigation: Avoid submitting private links or forwarding returned full URLs unless sharing their query tokens is acceptable.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of retrieved XHS data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include full note URLs with query tokens and partial paginated data.]

## Skill Version(s):

0.1.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents research Bilibili videos, articles, comments, reactions, and creators, with optional user-requested video downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use the skill to find and examine Bilibili content, discussions, engagement, and creator activity, or to save a video when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the latest npm release at runtime exposes the API key to package code that can change without review.

Mitigation: Prefer a pinned, reviewed package version or a trusted local installation before supplying the SocialDataX API key.

Risk: The download command saves video files to the local filesystem.

Mitigation: Run downloads only for videos the user explicitly requests and choose the output location deliberately.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown or plain text, with optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video downloads write files locally only when requested.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

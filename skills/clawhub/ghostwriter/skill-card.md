## Description:

Ghostwriter helps an agent interview the user for source material, then assemble writing from the user's own words instead of inventing new content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users, employees, and writing-focused teams use this skill when they need a draft for an audience and want the agent to interview them first, preserve their wording, and avoid inventing missing lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad writing requests and shift the agent into an interviewing workflow.

Mitigation: Use it when an interview-led writing process is desired, or ask the agent to avoid the ghostwriter workflow for ordinary drafting.

Risk: Optional context scouting may cause the agent to research a subject or destination before the interview.

Mitigation: Allow context scouting only when external research is acceptable for the task and subject matter.

Risk: User answers may include credentials, tokens, passwords, API keys, or private URLs.

Mitigation: Do not repeat secrets in the draft; replace them with a neutral description and ask the user for a placeholder.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/ghostwriter)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/ghostwriter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or prose draft assembled from interview answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include follow-up questions before drafting; excludes credentials and secrets from the draft.]

## Skill Version(s):

0.1.2 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

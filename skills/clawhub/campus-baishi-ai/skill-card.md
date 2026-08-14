## Description:

校园百事 is a Chinese campus life guide skill for new students and campus communities to query and share school-specific forum records about dining, empty classrooms, dorm life, nearby activities, warnings, Q&A, rankings, reports, and campus updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kangleizhui](https://clawhub.ai/user/kangleizhui)

### License/Terms of Use:

MIT-0

## Use Case:

External students and campus community members use this skill to bind a school, retrieve existing campus forum posts, interpret posts and images, submit or correct campus information, ask anonymous questions, view rankings, and report unsuitable content. The skill is intended for Chinese-language campus workflows backed by the named forum service rather than open-ended web knowledge.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks users to provide forum credentials in chat and stores them persistently in plaintext in a local JSON file.

Mitigation: Install only when this credential-handling model is acceptable; do not use reused passwords, restrict access to the local account file, and prefer direct login, OAuth, or revocable tokens in safer deployments.

Risk: The skill sends user-provided credentials and campus actions to the named forum service.

Mitigation: Confirm the service domain with users before collecting credentials and keep credential use limited to the documented forum registration, login, posting, and school lookup workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kangleizhui/skills/campus-baishi-ai)
- [Flarum read API reference](references/flarum-read-api.md)
- [Campus forum service](https://xysq.kcucu.com)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown, Configuration]

**Output Format:** [Chinese Markdown/plain text instructions with JSON and HTTP endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to persist forum credentials in data/accounts.json and call xysq.kcucu.com APIs.]

## Skill Version(s):

1.0.6 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

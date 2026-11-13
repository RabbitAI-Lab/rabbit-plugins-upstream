## Description:

Creates a complete picture book from a theme, with paged story text, consistent illustrations, matching background music, and a self-contained HTML reader.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating picture books, storybooks, or bedtime stories use the skill to turn a theme into a paged story with illustrations, music, and an HTML book for reading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign with medium confidence, but its evidence is incomplete and two items were flagged for review.

Mitigation: Review unresolved paths and the flagged items, and check that the host permissions fit your needs before running the skill.

Risk: Prompts and local reference images are sent to dLazy hosted services for illustration and music generation.

Mitigation: Avoid including sensitive information in prompts or reference images unless you are comfortable sending it to those services.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Images, Audio, HTML]

**Output Format:** [Self-contained HTML picture book with supporting image and audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; page count can follow the user's brief.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

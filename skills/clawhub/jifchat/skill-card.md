## Description:

Generate images and videos in the user's JifChat canvas when asked for creative media, with results saved to a canvas project and charged to their JifChat credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jifchat](https://clawhub.ai/user/jifchat)

### License/Terms of Use:

MIT-0

## Use Case:

People using JifChat can create and organize generated images and short videos in their own canvas projects, including product shots, posters, and UGC-style clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Declining a video run triggers project deletion.

Mitigation: Require separate approval before deleting a project.

Risk: Video-stitching commands can overwrite local files.

Mitigation: Use an isolated working directory with overwrite protection.

Risk: Uploaded media is shared with JifChat and its generation providers, and API keys can be exposed if mishandled.

Mitigation: Upload only media the user is comfortable sharing and protect the API key. Use a base-URL override only for an environment the user controls.

## Reference(s):

- [JifChat](https://jif.dev)
- [One-shot reference](references/one-shot.md)
- [Character consistency reference](references/character-consistency.md)

## Skill Output:

**Output Type(s):** [Images, Videos, API Calls]

**Output Format:** [Generated media in a JifChat canvas project]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets use the user's JifChat credits.]

## Skill Version(s):

1.0.1 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Collect YouTube video-post records by URL, search filters, hashtag, podcast URL, keyword, or Explore URL. Use for video discovery or lists. Do not use to download media files or retrieve only one video's metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify collection jobs for YouTube video-post discovery across channel URL, search-filter, hashtag, podcast URL, keyword, and Explore URL modes, then retrieve the final result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can launch quota-consuming Dataify collection jobs using a local API TOKEN.

Mitigation: Configure DATAIFY_API_TOKEN through a local environment variable or secret store, never paste it into chat, and require confirmation before broad, high-volume, or paid collection tasks.

Risk: Security evidence reports inconsistent guidance about media downloads and token handling.

Mitigation: Use the skill only for YouTube video-post collection, do not use it for media downloads, and review token-handling instructions before installation.

## Reference(s):

- [Modes and parameters](references/modes-and-parameters.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-video-post)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits one Dataify Builder task, monitors the returned task_id by default, and returns or summarizes the final JSON result.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

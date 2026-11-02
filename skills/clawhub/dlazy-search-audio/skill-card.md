## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection. Use 2-3 short English style keywords (e.g. 'upbeat pop energetic'); a long phrase or sentence returns zero results. Each hit's track URL is in the `url` field.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating audio or video content use the skill to search for background music with short English style keywords and review track URLs and metadata when choosing a track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches may consume dLazy credits.

Mitigation: Use `--dry-run` to review the payload and cost estimate before submitting a search.

Risk: Logging in saves an organization API key in the local CLI configuration.

Mitigation: Use the documented environment-variable alternative when appropriate, keep the key private, and rotate or revoke it from the organization dashboard if needed.

Risk: The example command conflicts with the documented query option.

Mitigation: Check `dlazy search_audio -h` and review the pinned CLI before installing; use the documented `--query` option.

## Reference(s):

- [CLI repository link (skill metadata)](https://github.com/dlazy-ai/cli)
- [CLI package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Track URLs, Audio metadata]

**Output Format:** [JSON response containing track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Track URLs are provided in each result's `url` field.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

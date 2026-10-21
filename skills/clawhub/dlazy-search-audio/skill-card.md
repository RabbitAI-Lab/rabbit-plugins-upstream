## Description:

Searches Pixabay Music for royalty-free tracks and returns URLs and metadata for selecting background music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find royalty-free background music by style and duration and review matching track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI and API can access credentials and may upload local files when file paths are supplied.

Mitigation: Review the CLI before installation, limit use to simple audio-search terms, and avoid local file paths or sensitive prompts.

Risk: Persisted API credentials may remain on the local machine.

Mitigation: Prefer per-invocation DLAZY_API_KEY over saved credentials when possible.

Risk: Search queries and possibly files may reach dLazy-hosted services rather than Pixabay directly.

Mitigation: Only submit content suitable for the third-party service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON search results containing track URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each result's track URL appears in the url field; searches work best with two or three short English style keywords.]

## Skill Version(s):

1.3.33 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

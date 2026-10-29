## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can search for background music by entering a few short English style keywords, then review matching track URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search text is sent to dLazy, and API requests may use account credits.

Mitigation: Use non-sensitive search terms and review command help or dry-run details before making requests.

Risk: The CLI saves a reusable API key in a local configuration file when logging in.

Mitigation: Protect access to the local config and rotate or revoke the key from the dLazy dashboard if needed.

Risk: The example command uses --prompt, while the documented search option is --query.

Mitigation: Check `dlazy search_audio -h` and use the option shown by the installed CLI.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON search results with track URLs and metadata, plus usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are best with 2–3 short English style keywords.]

## Skill Version(s):

1.3.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

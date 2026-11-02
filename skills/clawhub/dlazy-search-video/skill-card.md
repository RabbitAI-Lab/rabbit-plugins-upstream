## Description:

Searches Pixabay videos by keyword and returns stock video URLs and metadata for sourcing footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers can search for stock footage by keyword, type, category, or duration and use the returned video URLs and metadata in their workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches pass through dLazy and may consume credits.

Mitigation: Check the estimated cost with --dry-run where appropriate and confirm the account has sufficient credits before searching.

Risk: The skill saves an API key in the local CLI configuration, and search prompts and parameters are sent to dLazy.

Mitigation: Use an organization key you control, protect the local configuration file, avoid sending sensitive information, and review dLazy's data terms. Rotate or revoke the key if needed.

Risk: The example command uses --prompt while the listed search option is --query.

Mitigation: Check `dlazy search_video -h` and use the option shown by the installed CLI.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video URLs, Search metadata]

**Output Format:** [JSON search results containing stock video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports pagination and optional local downloads.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Searches PikPak cloud-drive file names and paths using keywords or regular expressions, with sorting and file-type options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can locate cloud-drive files by name or path when the CLI's search command is unavailable, then review matching paths, sizes, and dates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searching with an existing PikPak CLI session exposes cloud-drive file names and paths to the agent and its response.

Mitigation: Use only with an authorized session and treat search results as sensitive; avoid sharing paths or names beyond the intended audience.

Risk: The documented folder-search option does not return folders in the provided script.

Mitigation: Do not rely on folder-only results until the publisher fixes or clarifies this option.

Risk: Full-drive traversal can take a long time on large drives and stop at file or folder limits.

Mitigation: Scope searches to a relevant subfolder when possible and narrow the search if the traversal limit is reached.

## Reference(s):

- [PikPak Search on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-search)
- [PikPak CLI](https://mypikpak.com/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text results or optional JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Matching file paths, names, sizes, timestamps, and result counts; JSON output is optional.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

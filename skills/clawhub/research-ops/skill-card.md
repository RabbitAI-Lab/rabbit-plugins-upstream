## Description:

Organizes research projects across local files, Zotero, Obsidian, and Feishu using a single source of truth for each content type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomuiv](https://clawhub.ai/user/tomuiv)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and research teams use this skill to set up project directories, maintain a project index, map resources across research tools, and check cross-device synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled credential utilities can store and retrieve secrets, access the OS keyring, and run configured hooks after secret updates.

Mitigation: Review the credential utilities before installation; remove the creds/ directory if it is not needed, and run only trusted hooks.

## Reference(s):

- [ClawHub research-ops release](https://clawhub.ai/tomuiv/skills/research-ops)
- [Skill documentation](README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Configuration instructions]

**Output Format:** [Markdown guidance and JSON results from optional workspace scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional scripts can create project files or report workspace issues.]

## Skill Version(s):

1.0.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

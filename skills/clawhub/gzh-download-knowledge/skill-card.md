## Description:

Exports articles from the user's own WeChat Official Account publishing history into local Markdown files for archival and knowledge-base use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content owners use this skill to archive their own WeChat Official Account articles from the official publishing history into local Markdown files and JSON indexes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe output-file handling could overwrite files outside the intended export folder when untrusted output_files paths are used.

Mitigation: Run only with input.json files you create and trust, avoid output_files until the issue is fixed, and use a contained working directory or account when possible.

Risk: The skill uses the user's logged-in WeChat browser session through webclaw3 and saves article contents locally.

Mitigation: Run it only for the intended account, confirm the active browser login before use, and store outputs in a location appropriate for the article contents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/gzh-download-knowledge)
- [Publisher profile](https://clawhub.ai/user/fatmind)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [markdown, json, text]

**Output Format:** [Markdown article files, JSON status and index files, and a one-line JSON stdout summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports are written locally; article files include title, author, URL, and date metadata when available.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Archive Smart Reader helps agents list, preview, search, and extract files from zip, tar, gz, tgz, bz2, xz, 7z, and rar archives without a separate manual extraction step.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect archive contents, preview selected files, search filenames, and extract one or more files while working with compressed inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may modify the environment by installing Python packages or using locally discovered archive tools.

Mitigation: Prefer manually installed trusted archive tools, review dependency installation behavior, and verify local unrar or 7z paths before enabling rar or 7z preview and extraction.

Risk: Extracting untrusted archives can write files into unintended or sensitive directories.

Mitigation: Inspect archive contents first and extract only into dedicated temporary or working directories that do not contain sensitive files.

Risk: The skill keeps persistent usage and error records in a local learning file.

Mitigation: Periodically inspect or delete ~/.workbuddy/skills/archive-smart-reader/learned_patterns.json and disclose this persistence to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/archive-smart-reader)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown and terminal-style text with Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write extracted files and a local learned_patterns.json usage file when the skill is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

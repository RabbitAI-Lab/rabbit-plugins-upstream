## Description:

Skill Injection Scanner scans agent skill files for hidden instructions and prompt-injection patterns in English and Russian, then reports local findings for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT

## Use Case:

Developers, skill maintainers, and security reviewers use this skill to scan local agent skill directories before installation or reuse. It helps identify hidden prompt-injection patterns, suspicious instruction overrides, obfuscation, and remote fetch-and-run language in skill markdown, scripts, and configuration files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hostile skill package with symlinks could cause scanned snippets to come from files outside the intended folder.

Mitigation: Scan only directories the user explicitly approves, confirm the target path before running, and inspect untrusted packages for symlinks before scanning.

Risk: Using an unreviewed npm execution path could run package code outside the bundled scanner file.

Mitigation: Use the bundled `python3 scanner.py` path for reviewed releases; pin and independently verify any npm package path before use.

Risk: Findings printed to stdout may include snippets from scanned files, including credential-looking text.

Mitigation: Keep scans local, limit scope to the intended skills folder, and avoid saving or sharing output until snippets have been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vnbochkarev-netizen/skills/skill-injection-scanner)
- [GitHub repository](https://github.com/vnbochkarev-netizen/skill-injection-scanner)
- [npm package](https://www.npmjs.com/package/@vibo-dev/skill-injection-scanner)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; scanner findings print as terminal text or JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local scan output can include file paths, line numbers, rule names, severity labels, and short snippets from scanned files.]

## Skill Version(s):

1.1.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

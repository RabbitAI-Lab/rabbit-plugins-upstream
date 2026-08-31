## Description:

Helps agents run a pre-publication quality gate for skills, expert packages, documents, and tools by checking for sensitive information and guiding post-release self-tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, maintainers, and publishing reviewers use this skill before sharing or listing a release to check for company, local-machine, personal, and secret material, then document post-release TRACE self-test results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner output may display snippets that contain sensitive text from the files being reviewed.

Mitigation: Run it only on intended release folders, review terminal output locally, and avoid sharing logs until any sensitive snippets are removed.

Risk: Package attestation hashes alone may not prove the integrity of this submitted copy.

Mitigation: Confirm the submitted artifact against the server release hash and file hashes before relying on the attestation.

Risk: Pattern-based sensitive-information scans can produce false positives or miss context-specific secrets.

Mitigation: Manually review scanner findings and combine this quality gate with deeper security review for high-risk releases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/publish-quality-gate)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and scanner findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file paths, matched snippets, and pass/fail review recommendations when the local scanner is used.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter and manifest state 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

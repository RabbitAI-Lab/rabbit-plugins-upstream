## Description:

Checks whether existing contacts have changed jobs and identifies their new roles and companies when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams check existing contacts for job moves, identify former champions at new companies, and prioritize follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact details and session attribution may be sent to Cargo.

Mitigation: Use only with approval to share contact and job-change data and session attribution with Cargo.

Risk: An unrelated GitHub-star request could use the user's GitHub account.

Mitigation: Do not run the star action unless the user explicitly asks for it.

Risk: Installing the CLI at its latest version can change the code being run.

Mitigation: Prefer a reviewed, pinned CLI version when installing.

Risk: Large or repeated contact checks can consume substantial credits.

Mitigation: Sample a small segment, estimate credits, and obtain approval before a full run.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Job-change monitoring recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/job-change-monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary or table of contact job-change results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports lowercase job_change_status values (moved, left, no_change, unknown) and updated person details for movers.]

## Skill Version(s):

1.1.2 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

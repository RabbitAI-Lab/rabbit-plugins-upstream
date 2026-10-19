## Description:

Guides Go developers in using an unofficial client to access and manage Val Town resources through its API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add authenticated Val Town API access to their applications, including managing vals, files, storage, and account services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed API token could grant access to the user's Val Town account.

Mitigation: Use a least-privilege token where available, store it in VALTOWN_API_TOKEN, and never commit or log it.

Risk: Deleting resources, writing SQL, or sending email can change the user's account.

Mitigation: Review these requests and run them only when the user explicitly authorizes the changes.

## Reference(s):

- [go-valtown on ClawHub](https://clawhub.ai/psyb0t/skills/go-valtown)
- [Setup and API reference](references/setup.md)
- [go-valtown package documentation](https://pkg.go.dev/github.com/psyb0t/go-valtown)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Val Town API token for authenticated requests.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

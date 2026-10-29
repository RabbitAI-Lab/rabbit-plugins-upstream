## Description:

Searches Pixabay for stock videos by keyword and returns video URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to find stock video footage by keyword, with optional type, category, duration, and pagination filters. It returns video links and descriptive metadata for reviewing footage options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The usage example passes --prompt, while the documented search option is --query, which may cause the command to fail.

Mitigation: Check `dlazy search_video -h` and use the option names shown there; the documented keyword option is `--query`.

Risk: Searches may consume dLazy credits, and the CLI stores the organization API key in its local configuration after login.

Mitigation: Use `--dry-run` to review the payload and cost estimate first, and keep the local CLI credential configuration accessible only to its intended OS user.

Risk: Local media paths passed to supported media fields are uploaded to dLazy media storage.

Mitigation: Only provide files that you intend to upload to the service.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Video URLs, Video metadata]

**Output Format:** [JSON result envelope with video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters and pagination are supported; results can be saved locally, and asynchronous calls can return a task identifier.]

## Skill Version(s):

1.3.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

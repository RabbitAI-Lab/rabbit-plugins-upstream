## Description:

Deploy small, non-sensitive static sites to temporary Cloudflare Workers previews. Use when an intended user explicitly accepts Cloudflare terms and needs a short-lived workers.dev URL with a privately delivered Claim URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wei840222](https://clawhub.ai/user/wei840222)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to publish small, non-sensitive static directories as short-lived Cloudflare Workers preview URLs after explicit acceptance of Cloudflare terms. It returns a live workers.dev URL and keeps the Claim URL private for the intended user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected static directory is published to a public Cloudflare workers.dev URL.

Mitigation: Use only a trusted, stable directory containing public, non-sensitive files.

Risk: Cloudflare terms could be accepted without the intended user's informed consent.

Mitigation: Show the user Cloudflare terms and privacy policy and proceed only after explicit acceptance.

Risk: A Claim URL can transfer control of the temporary deployment if exposed.

Mitigation: Write the Claim URL to a private file and deliver it only to the intended user.

## Reference(s):

- [Cloudflare Temporary Preview Reference](references/cloudflare-api.md)
- [Cloudflare Workers Temporary Accounts](https://developers.cloudflare.com/workers/platform/claim-deployments/)
- [Cloudflare Workers Multipart Upload Metadata](https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/)
- [Cloudflare Workers Limits](https://developers.cloudflare.com/workers/platform/limits/)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown with inline shell command and URL text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a private Claim URL file and produce a public workers.dev preview URL for the selected static site.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

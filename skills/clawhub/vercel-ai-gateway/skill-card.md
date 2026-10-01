## Description:

Helps agents browse Vercel AI Gateway models and pricing, monitor credits and usage, and route inference requests through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can compare available AI models and provider pricing, check gateway credits and usage, and make authorized inference requests. With separate approval, they can set up hosted functions and automations using supported event sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the connection permits access to the user's Vercel AI Gateway account.

Mitigation: Get explicit approval before connecting; request only necessary scopes and keep credentials in the operating system's credential store.

Risk: Inference requests may incur charges, and write operations may change account state.

Mitigation: Default to read-only calls and confirm paid inference and each write with the user before proceeding.

Risk: Hosted functions, trigger destinations, and event watchers can continue acting or forwarding sensitive data after setup.

Mitigation: Obtain separate approval for each automation and destination, disclose what data will flow where, and only run reviewed handlers on untrusted event data.

## Reference(s):

- [Vercel AI Gateway skill release](https://clawhub.ai/maton/skills/vercel-ai-gateway)
- [Maton homepage](https://maton.ai)
- [Vercel AI Gateway REST API](https://vercel.com/docs/ai-gateway/sdks-and-apis/rest-api)
- [Vercel AI Gateway pricing and credits](https://vercel.com/docs/ai-gateway/pricing)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, code, and API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live API results depend on the user's connection, account permissions, model availability, and plan.]

## Skill Version(s):

1.2.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

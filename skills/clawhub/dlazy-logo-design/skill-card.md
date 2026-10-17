## Description:

Helps create, refine, and evaluate brand logos, delivering a transparent-background logo and previews across common brand contexts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and other users create, update, or assess logos and preview them in light, dark, app icon, favicon, and business-card contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files may be sent to dLazy's hosted service.

Mitigation: Review prompts and attachments before sending; avoid sharing confidential material without authorization.

Risk: Login can store a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials; use a per-invocation environment variable when persistence is undesirable and rotate or revoke keys if exposed.

Risk: A global CLI installation persists on the user's system.

Mitigation: Use the documented pinned npx invocation when a global installation is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI repository (listed in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Images]

**Output Format:** [CLI chat response with a transparent-background logo and multi-context previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up conversations are supported.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

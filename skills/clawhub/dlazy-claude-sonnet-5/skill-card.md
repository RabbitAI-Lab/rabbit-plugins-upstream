## Description:

Anthropic's latest Sonnet — near-Opus quality on coding and long-horizon agentic work at Sonnet cost, with support for text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can request text, code, or structured responses from dLazy's hosted Claude Sonnet 5 service. The skill also supports requests that include image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the CLI package was not inspected and its install and login instructions were not clearly explained in relation to the skill's purpose.

Mitigation: Review the CLI package, account setup, and service details before installing or authenticating.

Risk: Prompts and local image or video files may be sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive prompts or media unless the service's handling terms are acceptable.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response envelope containing generated content; content varies by prompt.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts image and video inputs. Local media files may be uploaded to dLazy's hosted storage.]

## Skill Version(s):

1.2.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

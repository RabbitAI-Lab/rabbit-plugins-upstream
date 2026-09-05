## Description:

Seedance 2.5 Image to Video animates one still image into a 4-30 second 720p clip with optional synchronized native audio through the RunComfy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[permew](https://clawhub.ai/user/permew)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill to animate a single approved still image into a short video clip with optional in-pass speech, sound effects, or music. It is suited to product packshots, portrait animation, social ad variants, talking-head clips, and previsualization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or authenticating with an untrusted CLI package or account flow could expose credentials.

Mitigation: Confirm the RunComfy CLI package and account flow are trusted before installation or use.

Risk: Private image URLs or token-bearing query strings are fetched by RunComfy servers.

Mitigation: Use only image URLs intended for server-side fetches and avoid embedding private tokens in URLs.

Risk: Generations are billed per second.

Mitigation: Confirm duration and billing expectations before running jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/permew/skills/seedance-2-5-image-to-video)
- [RunComfy homepage](https://www.runcomfy.com)
- [Seedance 2.5 Image to Video model page](https://www.runcomfy.com/models/bytedance/seedance-2.5/image-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=seedance-2-5-image-to-video&utm_content=bytedance-seedance-2.5-image-to-video)
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=seedance-2-5-image-to-video&utm_content=cli-docs-troubleshooting)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with bash commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides RunComfy CLI calls that produce 720p video clips with optional native audio.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

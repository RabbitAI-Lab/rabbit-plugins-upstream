## Description:

Helps agents use a self-hosted video API to lip-sync footage, restore faces, edit and transcode media, and inspect video metadata through REST or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media creators use this skill to direct a self-hosted video service to lip-sync faces, restore footage, perform common editing operations, and retrieve metadata or processed files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default container setup may expose an unauthenticated video-processing API to the network.

Mitigation: Run on a trusted host, bind the published port to loopback, set FLICKIES_AUTH_TOKEN, and do not expose the API directly to untrusted networks.

Risk: Uploads, remote media inputs, output destinations, and webhook URLs can share media or results beyond the local host.

Mitigation: Use only approved local media and explicitly authorized URLs for remote inputs, outputs, and callbacks.

Risk: Unpinned container images can change between deployments.

Mitigation: Pin Docker images to a version or digest when possible.

## Reference(s):

- [flickies setup guide](references/setup.md)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/flickies)
- [flickies project homepage](https://github.com/psyb0t/docker-flickies)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide retrieval of processed video, audio, thumbnails, and metadata from the configured service.]

## Skill Version(s):

0.3.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

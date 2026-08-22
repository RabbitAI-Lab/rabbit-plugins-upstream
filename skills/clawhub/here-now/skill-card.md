## Description:

here.now lets agents publish websites and files to live URLs and manage private Drive storage, workspace publishing, and access controls through here.now scripts and APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to publish local files or folders as live here.now sites, update existing sites, manage access, and use private Drive storage for persistent agent files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected files to here.now and publish them as live sites.

Mitigation: Review the files and access mode before publishing; use password, restricted, or workspace member access when content should not be public.

Risk: The skill stores long-lived here.now credentials locally.

Mitigation: Store credentials only in the documented credentials file with restrictive permissions, avoid command-line API key flags in interactive sessions, and never commit credentials or local state files.

Risk: Drive sharing can create broad tokens, including full-Drive access when no path prefix is set.

Mitigation: Use the narrowest path prefix, prefer read-only access unless write access is required, set a short TTL, and revoke tokens when they are no longer needed.

Risk: The security evidence reports a suspicious verdict because broad Drive sharing and persistent credentials have limited built-in safeguards.

Mitigation: Install only when those behaviors are acceptable for the environment and require explicit review before sharing Drive access or publishing sensitive files.

## Reference(s):

- [here.now documentation](https://here.now/docs)
- [here.now workspaces](https://here.now/docs#workspaces)
- [here.now access control](https://here.now/docs#access-control)
- [here.now workspace access](https://here.now/docs#workspace-access)
- [here.now version history](https://here.now/docs#versions)
- [here.now public profiles](https://here.now/docs#profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Text]

**Output Format:** [Markdown with inline shell commands and URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update hosted sites, local publish state, credentials files, and Drive share tokens when the agent runs the provided helper scripts.]

## Skill Version(s):

1.21.1 (source: evidence release and skill body)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Find Skills helps agents discover, compare, vet, and optionally install agent skills by searching skills.sh, ClawHub, and GitHub from one workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[permew](https://clawhub.ai/user/permew)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to find relevant published skills across multiple registries, compare registry-native popularity signals, scan top candidates for risky patterns, and choose or install a suitable skill for a task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security source marks the release suspicious because installation guidance can help install third-party skills globally.

Mitigation: Use a version-pinned Skills CLI and review any recommended third-party skill before installing it.

Risk: The security source notes that the skill reads locally installed skill names and queries public registries.

Mitigation: Use it only when sharing the search query and installed skill names with local tooling and public registry endpoints is acceptable.

Risk: The security source notes that /tmp/find-skills-*.json reports may persist after use.

Mitigation: Delete generated /tmp/find-skills-*.json reports when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/permew/skills/find-skills)
- [Publisher profile](https://clawhub.ai/user/permew)
- [Skill homepage](https://agentspace.so)
- [skills.sh search API](https://skills.sh/api/search)
- [ClawHub search API](https://clawhub.ai/api/search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown report or machine-readable JSON, with shell commands for optional installation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a persistent local report under /tmp/find-skills-*.json; requires jq and curl, with optional gh and unzip for richer registry and scan results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

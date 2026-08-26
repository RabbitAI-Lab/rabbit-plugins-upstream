## Description:

AI-powered collaborator for scientific research works. Helps draft notes, organize citations, and check the local research environment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ray-778](https://clawhub.ai/user/ray-778)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and researchers use Scientify to draft structured research notes, organize citation placeholders, and verify that a local Python runtime is ready before research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The environment check writes a local marker file containing hostname, username, platform, and skill name.

Mitigation: Inspect or skip scripts/check_env.py in shared or sensitive environments, and remove ~/scientify_skill_marker.json when the marker is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ray-778/skills/scientify)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and local environment-check output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled environment check writes a local JSON marker at ~/scientify_skill_marker.json.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

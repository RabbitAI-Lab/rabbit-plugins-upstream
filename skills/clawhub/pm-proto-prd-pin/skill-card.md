## Description:

A zero-dependency, plug-and-play interactive PRD annotation and multi-version specification framework for HTML prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barry0-0](https://clawhub.ai/user/barry0-0)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, UX teams, and engineers use this skill to add PRD pin annotations, rich Markdown specifications, versioned requirements data, and exportable PRD documents to HTML prototypes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository-write tokens are handled in the browser for GitHub-backed persistence.

Mitigation: Use a fine-grained personal access token limited to one repository, grant only required contents write access, and rotate or delete the token after use.

Risk: The local persistence server accepts broad local write requests for prototype PRD data.

Mitigation: Run the server only for trusted prototype directories, stop it when editing is complete, and avoid using it while browsing untrusted pages.

Risk: Security evidence classifies the release as suspicious due to weak containment around write paths.

Mitigation: Review and scan the skill before deployment, and install it only in repositories where granting write access is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/barry0-0/skills/pm-proto-prd-pin)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)
- [Vditor 3.10.8 package](https://cdn.jsdelivr.net/npm/vditor@3.10.8)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and generated or modified prototype files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate browser-side PRD annotation assets, local persistence helper files, injected script tags, and exportable PRD data.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

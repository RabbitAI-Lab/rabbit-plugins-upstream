## Description: <br>
Routes agents to the right Cargo CLI skill and explains setup, workflows, UUID conventions, async polling, use cases, and common gotchas for Cargo workspaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and GTM operators use this router when working with Cargo CLI skills to choose the right capability skill, bootstrap workspaces, stitch tasks together, and manage Cargo workspace workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to refresh tools and skills and may use lifecycle hooks that affect local tooling or session records. <br>
Mitigation: Prefer the npm or OpenClaw install path, inspect any curl-to-shell installer before use, and confirm the active workspace before writes. <br>
Risk: The skill can send session or report data to Cargo services when the user consents. <br>
Mitigation: Ask before sharing, omit secrets and record-level data, and skip reporting when the user declines. <br>
Risk: Cargo CLI access can affect workspace resources through token creation, deploys, removals, deletes, or paid actions. <br>
Mitigation: Watch prompts carefully and require explicit user confirmation before sensitive, destructive, or paid operations. <br>


## Reference(s): <br>
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills) <br>
- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo) <br>
- [Glossary](references/glossary.md) <br>
- [Interaction conventions](references/interaction.md) <br>
- [Cargo CLI prerequisites](references/prerequisites.md) <br>
- [End-to-end use cases](references/use-cases.md) <br>
- [UUID flow between skills](references/uuid-flow.md) <br>
- [Common gotchas](references/gotchas.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires @cargo-ai/cli and a Cargo account; Cargo commands generally return JSON.] <br>

## Skill Version(s): <br>
1.15.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

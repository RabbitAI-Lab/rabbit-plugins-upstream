## Description:

Guides a first-run Cargo demo that asks one buyer-persona question, pulls about 25 leads, shows a cost receipt, and offers to save the workflow as a recurring play.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers evaluating Cargo use this skill to run a guided lead-sourcing quickstart. It helps an agent ask one persona question, run the Cargo CLI, present lead results with cost context, and optionally prepare a recurring play.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Cargo credits while sourcing leads.

Mitigation: Confirm the expected credit spend before paid commands run and present the receipt after completion.

Risk: The skill can run account-affecting Cargo workflows, including saving a recurring play.

Mitigation: Confirm the active workspace, provider choice, and recurring play setup before allowing those commands to run.

Risk: The install path uses an unpinned @cargo-ai/cli@latest package.

Mitigation: Prefer a pinned Cargo CLI version when release or environment policy requires reproducible installs.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo Quickstart on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-quickstart)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and tabular lead summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide account-affecting Cargo CLI actions, credit-spending lead pulls, temporary JSON output handling, and recurring play setup after user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter, artifact metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

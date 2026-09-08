## Description:

Aws Wechat Article W guides an agent through drafting, rewriting, continuing, and polishing long-form WeChat public-account articles from a topic, outline, topic card, and local article configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to guide an agent through WeChat article drafting workflows. It supports article setup checks, draft generation, rewrite and continuation flows, local draft output, and optional model-backed writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the read-only install metadata does not match behavior that can run a Python writing script and update local workflow files.

Mitigation: Review the skill before installation, run it in a controlled workspace, and confirm expected file writes before allowing an agent to execute the workflow.

Risk: The skill can send article materials and WRITING_MODEL_API_KEY to a configured external model endpoint.

Mitigation: Use a dedicated writing-model API key, configure only a trusted base_url or internal proxy, and use the prompt-only path when content should not be sent to a third-party endpoint.

Risk: The skill is part of a companion suite and may rely on sibling skills or shared references for the full workflow.

Mitigation: Install the companion suite only from a trusted source, or limit use to the steps that work with this skill's local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-wechat-article-writing)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with file paths, command examples, configuration updates, and generated article draft content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update draft.md and article workflow configuration files in the user's article workspace when executed by an agent.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

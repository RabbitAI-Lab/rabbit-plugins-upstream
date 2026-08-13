## Description:

Searches the Tizhuang question-bank service for real K12 primary, middle, and high school questions and helps agents deliver chat practice, temporary practice pages, quizzes, answer checking, and paper-builder handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weishao2](https://clawhub.ai/user/weishao2)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, learners, parents, and agent users use this skill to find real Chinese K12 questions by curriculum filters, create answer-hidden practice experiences, check answers, and hand off structured paper-building requests to the Tizhuang website.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts the remote Tizhuang question-bank service and can be pointed at a custom service URL.

Mitigation: Use the default service URL or another trusted HTTPS endpoint before running retrieval, practice-page, or paper-builder commands.

Risk: License keys, account tokens, and trial tokens are local credentials that could expose account access or quota if shared.

Mitigation: Store credentials only in local environment configuration or the local cache, and never paste them into chat, URLs, prompts, output, or logs.

Risk: Public paper-share options can expose standard answers or remove watermarks when explicitly enabled.

Mitigation: Use the safe default of questions only with a visible watermark unless the user explicitly requests answer exposure or watermark removal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weishao2/skills/tizhuang-question-bank)
- [Server-resolved GitHub provenance](https://github.com/weishao2/tizhuang-agent-skills/tree/main/skills/question-bank)
- [Tizhuang question service API](https://tizhuang.qcscience.cc/api)
- [API reference](references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with CLI command examples, JSON-backed results, and returned practice or builder URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Question content, answers, and explanations should be preserved from the service; practice-page and paper-builder links are generated through the bundled CLI.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

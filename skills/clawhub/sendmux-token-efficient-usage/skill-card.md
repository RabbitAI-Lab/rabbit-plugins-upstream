## Description: <br>
Choose low-token Sendmux calls across MCP, CLI, SDKs, and HTTP by using snippets, counts, batches, deltas, cursors, ETags, and idempotency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to choose efficient Sendmux operations for authorized email, mailbox, management, and API workflows while minimizing unnecessary reads, sends, retries, and attachment transfer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may access Sendmux keys or agent tokens while performing authorized workflows. <br>
Mitigation: Keep key and token scopes narrow, use the appropriate Sendmux credential type for each surface, and do not ask users to paste secrets into chat. <br>
Risk: Sends, deletes, provider changes, and other account-impacting actions can have side effects. <br>
Mitigation: Require explicit approval for account-impacting actions and use idempotency keys for supported mutations and retries. <br>
Risk: Full mailbox reads, broad log scans, or inline attachment transfer can expose unnecessary content and consume excess context. <br>
Mitigation: Prefer counts, snippets, small limits, batch reads, deltas, cursors, ETags, and file paths or presigned URLs for attachments. <br>


## Reference(s): <br>
- [Sendmux skills repository](https://github.com/Sendmux/skills) <br>
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-token-efficient-usage) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions] <br>
**Output Format:** [Markdown with tables and inline bash/code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides route, batching, pagination, idempotency, and attachment-handling guidance for Sendmux workflows.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata; artifact frontmatter says 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
